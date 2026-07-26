from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

out = Path(r"C:/Users/rushi/OneDrive/Documents/GitHub/DevOps-Project-ProductionAppDeployment/portfolio-website/assets/Rushikesh_Deshmukh_Resume.pdf")
out.parent.mkdir(parents=True, exist_ok=True)
navy, blue, slate = colors.HexColor("#102A43"), colors.HexColor("#1D5FA7"), colors.HexColor("#334E68")
s = getSampleStyleSheet()
s.add(ParagraphStyle(name="name", fontName="Helvetica-Bold", fontSize=20, leading=23, textColor=colors.white))
s.add(ParagraphStyle(name="head", fontName="Helvetica", fontSize=9.5, leading=12, textColor=colors.HexColor("#EAF2F8")))
s.add(ParagraphStyle(name="contact", fontName="Helvetica", fontSize=8.3, leading=11, textColor=colors.white, spaceBefore=4))
s.add(ParagraphStyle(name="section", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=navy, spaceBefore=7, spaceAfter=2))
s.add(ParagraphStyle(name="body", fontName="Helvetica", fontSize=8.4, leading=10.5, textColor=colors.HexColor("#1F2933")))
s.add(ParagraphStyle(name="role", fontName="Helvetica-Bold", fontSize=9.1, leading=11, textColor=colors.HexColor("#1F2933")))
s.add(ParagraphStyle(name="company", fontName="Helvetica-Oblique", fontSize=8.3, leading=10, textColor=slate))
s.add(ParagraphStyle(name="bullet", parent=s["body"], leftIndent=9, firstLineIndent=-7, spaceAfter=1))

def para(x, style="body"): return Paragraph(x, s[style])
def section(x): return [Spacer(1, 2), para(x.upper(), "section"), Table([[""]], colWidths=[174*mm], rowHeights=[0.55*mm], style=TableStyle([("BACKGROUND", (0,0),(-1,-1),blue)])), Spacer(1, 2)]
def bullet(x): return para("- " + x, "bullet")
def job(role, dates, company, bullets):
    row = Table([[para(role,"role"), para(dates,"role")]], colWidths=[132*mm,42*mm], style=TableStyle([("ALIGN",(1,0),(1,0),"RIGHT"), ("VALIGN",(0,0),(-1,-1),"TOP")]))
    return [row, para(company,"company")] + [bullet(x) for x in bullets] + [Spacer(1,2)]

doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=13*mm, bottomMargin=12*mm)
story=[]
header = Table([[para("RUSHIKESH DESHMUKH","name")],[para("SRE | DevOps Engineer | MLOps Engineer","head")],[para('Pune, India | rushikeshdeshmukh0420@gmail.com | <link href="https://www.linkedin.com/in/rushikesh-d-150b271a9/"><font color="#FFFFFF">LinkedIn</font></link> | <link href="https://github.com/Rushi412"><font color="#FFFFFF">GitHub</font></link> | <link href="https://rushi412.github.io"><font color="#FFFFFF">Portfolio</font></link>',"contact")]], colWidths=[174*mm], style=TableStyle([("BACKGROUND",(0,0),(-1,-1),navy),("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),12),("TOPPADDING",(0,0),(-1,0),10),("BOTTOMPADDING",(0,-1),(-1,-1),10)]))
story += [header] + section("Professional Summary") + [para("SRE, DevOps, and MLOps engineer with 3+ years of experience delivering reliable cloud infrastructure, CI/CD pipelines, and Kubernetes platforms across AWS and GCP. Skilled in infrastructure as code, observability, secrets management, incident response, and reproducible ML systems. Focused on improving deployment reliability and enabling fast, safe releases.")]
story += section("Technical Skills") + [para("<b>Cloud:</b> AWS (EC2, S3, RDS, Lambda, EKS, IAM, CloudWatch, VPC) | GCP (GKE, GCS, Compute Engine, Cloud Functions, BigQuery, Pub/Sub)"), para("<b>DevOps:</b> Jenkins, GitHub Actions, Docker, Kubernetes (GKE, EKS), Istio, Terraform, Terraform Workspaces"), para("<b>MLOps:</b> MLflow, FastAPI, MinIO, PostgreSQL, experiment tracking, model artifact storage"), para("<b>Observability & Security:</b> Prometheus, Grafana, CloudWatch, HashiCorp Vault, VPC Service Controls, CMEK"), para("<b>Languages & Tools:</b> Python, Bash, Shell Script, Groovy, SQL, YAML, ServiceNow, Jira")]
story += section("Professional Experience")
story += job("Site Reliability Engineer","Jan 2026 - Present","Equifax, Pune, India",["Own reliability for a mission-critical GCP marketplace platform across seven environments, sustaining 99.9% service availability through Terraform Workspaces-driven infrastructure management.","Re-architected Terraform into modular, encrypted GCS-backed components for GKE, analytics, and ETL platforms, reducing deployment risk and accelerating provisioning.","Automated multi-stage Jenkins CI/CD delivery with shared libraries and short-lived HashiCorp Vault secrets, improving release consistency and eliminating manual release errors.","Designed secure GKE and analytics infrastructure with private clusters, VPC Service Controls, CMEK, auto-scaling, and cross-region disaster-recovery patterns."])
story += job("DevOps Engineer","Jul 2022 - Jul 2025","Tata Consultancy Services, Pune, India",["Operated and scaled containerized Kubernetes microservices supporting thousands of concurrent users.","Reduced manual provisioning effort by 70% through Terraform-based multi-region AWS infrastructure automation.","Engineered Jenkins CI/CD pipelines that improved deployment speed by 45% and reduced deployment failures by 25%.","Reduced critical production incidents by 30% by embedding CloudWatch and Prometheus observability into delivery workflows."])
story += section("Projects") + [para('<b>MLOps Learning Platform</b> (<link href="https://github.com/Rushi412/MLOps-project"><font color="#1D5FA7">GitHub Repository</font></link>): Built a local-first MLOps platform with MLflow, PostgreSQL, MinIO, FastAPI, Docker, Kubernetes, Prometheus, and Grafana. Implemented reproducible churn, loan-default, and demand-forecasting workflows with experiment tracking and model artifact storage.'), Spacer(1,3), para('<b>Social Platform App - DevOps Deployment</b> (<link href="https://github.com/Rushi412/DevOps-Project-ProductionAppDeployment"><font color="#1D5FA7">GitHub Repository</font></link>): Containerized and deployed a Spring Boot social platform application to a local kind Kubernetes cluster with secure Docker configuration, health checks, and Jenkins CI/CD automation with Trivy scanning and rollout verification.')]
story += section("Education & Certifications") + [para("<b>Bachelor of Technology in Electronics and Telecommunication</b> | SVERI, Solapur University, Solapur, India | 2018 - 2022"), Spacer(1,2), para("Google Cloud Certified: Associate Cloud Engineer | Google Cloud Certified: Generative AI Leader | Microsoft Certified: Azure DevOps Engineer Expert (AZ-400)")]
doc.build(story)
print(out)
