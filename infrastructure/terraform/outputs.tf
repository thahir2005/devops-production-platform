output "deployment_metadata_file" {
  description = "Path to the Terraform-generated deployment metadata"
  value       = local_file.deployment_metadata.filename
}

output "environment" {
  description = "Current deployment environment"
  value       = var.environment
}