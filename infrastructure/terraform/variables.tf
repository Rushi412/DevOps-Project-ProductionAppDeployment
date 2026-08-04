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

variable "confirm_paid_eks" {
  description = "Explicit acknowledgement that EKS and its supporting resources can incur AWS charges."
  type        = bool
  default     = false
}

variable "node_desired_size" {
  description = "Desired EKS managed node count for a temporary demonstration environment."
  type        = number
  default     = 1

  validation {
    condition     = var.node_desired_size >= 1 && var.node_desired_size <= 3
    error_message = "node_desired_size must be between 1 and 3 for this portfolio environment."
  }
}

variable "node_max_size" {
  description = "Maximum EKS managed node count."
  type        = number
  default     = 2
}
