variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "development"
}

variable "application_name" {
  description = "Application name"
  type        = string
  default     = "production-reliability-api"
}