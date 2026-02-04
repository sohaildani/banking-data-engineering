🏦 Banking Data Engineering Platform (Senior Data Engineer)

End-to-end PySpark data engineering project inspired by real-world banking platforms (ENBD-style).
Designed to demonstrate senior-level architecture, data modeling, and Spark best practices — not toy examples.

👤 Who this project is for

This repository is aimed at:

Senior / Lead Data Engineer roles

Banking, FinTech, Enterprise Data Platforms

Interview discussions around design, scalability, and governance

If you’re a recruiter or hiring manager: this repo reflects how data pipelines are actually built and explained in banks.

🚀 Project Summary

The platform simulates a banking analytics pipeline that processes:

Customer master data (KYC lifecycle)

Account balances

Financial transactions

Using a Medallion Architecture (Bronze → Silver → Gold), the system ensures:

Auditability

Historical tracking (SCD Type 2)

Clean separation of concerns

Re-runnable, idempotent jobs

🧱 Architecture Overview
Raw Sources (CSV / Landing Zone)
        │
        ▼
🟤 Bronze Layer  → Immutable raw ingestion (audit & replay)
        │
        ▼
⚪ Silver Layer  → Cleansed data + business logic
        │              • Data quality checks
        │              • SCD Type 2 (customer KYC history)
        ▼
🟡 Gold Layer   → Analytics-ready datasets & KPIs
        │
        ▼
BI / Reporting / ML
🧠 Key Engineering Concepts Demonstrated
✅ Medallion Architecture

Clear separation between raw, refined, and analytical layers — a standard pattern in large banks.

✅ SCD Type 2 (Customer Dimension)

Tracks historical KYC status changes using effective dates and current flags.

✅ Data Quality Enforcement

Explicit null checks and validation before promoting data downstream.

✅ Spark Performance Awareness

Adaptive Query Execution enabled

Controlled shuffle partitions

Centralized Spark configuration

✅ Idempotent & Re-runnable Pipelines

Jobs can be safely re-run without corrupting downstream layers.

📁 Repository Structure
banking-data-engineering/
├── config/        # Central Spark configuration
├── data/          # Sample raw input data
├── src/
│   ├── bronze/    # Raw ingestion layer
│   ├── silver/    # Cleansing & business logic
│   ├── gold/      # Analytics & KPIs
│   └── utils/     # Reusable Spark & data quality utilities
└── scripts/       # Pipeline execution scripts
▶ How to Run (Local)
pip install -r requirements.txt
bash scripts/run_pipeline.sh

Each layer executes independently and can be monitored or re-run in isolation.

🗣️ How to Discuss This in Interviews

Strong, senior-level talking points:

“We keep Bronze immutable for audit and regulatory replay.”

“Customer KYC history is modeled using SCD Type 2.”

“Silver applies data quality and business rules.”

“Gold is optimized for analytics and reporting, not transformations.”

“Spark configs are centralized to avoid environment drift.”

This project is intentionally structured to support design discussions, not just code walkthroughs.

🏦 Why This Matches Banking Environments

Regulatory-friendly design

Historical traceability

Clear data ownership per layer

Scalable Spark patterns used in production

This mirrors how pipelines are implemented in Emirates NBD–scale data platforms.

🔮 Possible Enhancements

Delta Lake + MERGE for true upserts

Airflow orchestration

Cloud storage (S3 / ADLS)

Schema evolution & governance

Fraud / AML analytical use cases

👋 Author

Mohd Sohail Khan
Senior Data Engineer

📌 GitHub: https://github.com/sohaildani
