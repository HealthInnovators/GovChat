data "terraform_remote_state" "GovChat" {
  backend   = "s3"
  workspace = terraform.workspace
  config = {
    bucket = var.state_bucket
    key    = "GovChat/terraform.tfstate"
    region = var.region
  }
}

data "terraform_remote_state" "platform" {
  backend   = "s3"
  workspace = terraform.workspace
  config = {
    bucket = var.state_bucket
    key    = "platform/terraform.tfstate"
    region = var.region
  }
}


provider "aws" {
  default_tags {
    tags = {
      "platform:environment"    = terraform.workspace
      "platform:repository"     = "https://github.com/i-dot-ai/GovChat"
      "platform:security-level" = "base"
      "platform:deployed-via"   = "github"

      Organisation  = "co"
      Department    = "i-dot-ai"
      "Cost Centre" = "i-dot-ai"
    }
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.53.0"
    }

    random = {
      source  = "hashicorp/random"
      version = ">=3.6.2"
    }
  }
  required_version = ">= 1.3.5"

  backend "s3" {
    key = "GovChat-postgres-deployment/terraform.tfstate"
  }

}
