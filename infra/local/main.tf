terraform {
  required_providers {
    kind = { source = "tehcyx/kind",     version = "~> 0.4" }
    helm = { source = "hashicorp/helm",  version = "~> 2.17" }
  }
}

resource "kind_cluster" "this" {
  name           = "platform-demo"
  wait_for_ready = true
}

provider "helm" {
  kubernetes {
    config_path = kind_cluster.this.kubeconfig_path
  }
}

resource "helm_release" "argocd" {
  name             = "argocd"
  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  create_namespace = true
}