variable "project_name" {
  description = "Prefix applied to provisioned resources."
  type        = string
  default     = "social-platform-app"
}

variable "environment" {
  description = "Deployment environment label."
  type        = string
  default     = "learning"
}

variable "aws_region" {
  description = "AWS region. ap-south-1 is selected for proximity, not because it is free."
  type        = string
  default     = "ap-south-1"
}

variable "node_instance_type" {
  description = "Smallest recommended EKS worker instance for this learning project."
  type        = string
  default     = "t3.medium"
}
