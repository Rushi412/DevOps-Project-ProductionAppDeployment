output "cluster_name" {
  value       = aws_eks_cluster.social_platform.name
  description = "EKS cluster name."
}

output "cluster_endpoint" {
  value       = aws_eks_cluster.social_platform.endpoint
  description = "EKS API server endpoint."
}

output "vpc_id" {
  value       = aws_vpc.social_platform.id
  description = "VPC ID for the Social Platform App environment."
}

output "subnet_ids" {
  value       = aws_subnet.social_platform[*].id
  description = "Subnet IDs used by the EKS cluster."
}
