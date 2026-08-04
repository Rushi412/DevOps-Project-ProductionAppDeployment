# EKS-ready Terraform

This configuration describes a small, temporary Amazon EKS demonstration environment. It does not create resources unless `terraform apply` is run.

EKS, EC2 nodes, networking, and storage can incur charges. The committed environment file keeps `confirm_paid_eks = false`, which deliberately blocks planning until a user explicitly acknowledges the cost.

## Safe validation (no AWS resources)

```powershell
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```

## Approved temporary demonstration only

```powershell
terraform plan -var-file=environments/demo.tfvars -var="confirm_paid_eks=true"
```

Do not apply that plan without a defined budget and cleanup window. After an approved demonstration, run `terraform destroy` and confirm that the EKS cluster, node group, VPC, and related resources are gone.
