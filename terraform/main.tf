terraform {
  required_version = ">= 1.0.0"
}

# Simple example resource (no cloud required)
resource "local_file" "dataops_demo" {
  filename = "demo_output.txt"
  content  = "DataOps Terraform setup is successful!"
}