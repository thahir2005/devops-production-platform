resource "local_file" "deployment_metadata" {
  filename = "${path.module}/deployment-metadata.json"

  content = jsonencode({
    application = var.application_name
    environment = var.environment
    managed_by  = "terraform"
    version     = "1.0.0"
  })
}