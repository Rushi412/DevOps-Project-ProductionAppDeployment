terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

data "aws_availability_zones" "available" {
  state = "available"
}

locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = "Rushikesh Deshmukh"
  }
}

resource "aws_vpc" "social_platform" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(local.common_tags, { Name = "${var.project_name}-vpc" })
}

resource "aws_subnet" "social_platform" {
  count                   = 2
  vpc_id                  = aws_vpc.social_platform.id
  cidr_block              = cidrsubnet(aws_vpc.social_platform.cidr_block, 8, count.index)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = merge(local.common_tags, {
    Name                                      = "${var.project_name}-subnet-${count.index + 1}"
    "kubernetes.io/cluster/${var.project_name}-cluster" = "shared"
  })
}

resource "aws_internet_gateway" "social_platform" {
  vpc_id = aws_vpc.social_platform.id
  tags   = merge(local.common_tags, { Name = "${var.project_name}-igw" })
}

resource "aws_route_table" "social_platform" {
  vpc_id = aws_vpc.social_platform.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.social_platform.id
  }

  tags = merge(local.common_tags, { Name = "${var.project_name}-public-routes" })
}

resource "aws_route_table_association" "social_platform" {
  count          = 2
  subnet_id      = aws_subnet.social_platform[count.index].id
  route_table_id = aws_route_table.social_platform.id
}

resource "aws_security_group" "cluster" {
  name        = "${var.project_name}-cluster"
  description = "EKS control-plane security group"
  vpc_id      = aws_vpc.social_platform.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(local.common_tags, { Name = "${var.project_name}-cluster-sg" })
}

resource "aws_eks_cluster" "social_platform" {
  name     = "${var.project_name}-cluster"
  role_arn = aws_iam_role.cluster.arn

  vpc_config {
    subnet_ids         = aws_subnet.social_platform[*].id
    security_group_ids = [aws_security_group.cluster.id]
  }

  tags = local.common_tags
}

resource "aws_eks_node_group" "social_platform" {
  cluster_name    = aws_eks_cluster.social_platform.name
  node_group_name = "${var.project_name}-nodes"
  node_role_arn   = aws_iam_role.node_group.arn
  subnet_ids      = aws_subnet.social_platform[*].id
  instance_types  = [var.node_instance_type]

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  tags = local.common_tags
}

resource "aws_iam_role" "cluster" {
  name = "${var.project_name}-cluster-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "eks.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cluster" {
  role       = aws_iam_role.cluster.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

resource "aws_iam_role" "node_group" {
  name = "${var.project_name}-node-group-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "node_group" {
  for_each = toset([
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  ])

  role       = aws_iam_role.node_group.name
  policy_arn = each.value
}
