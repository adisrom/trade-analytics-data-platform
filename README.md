# Trade Analytics Data Platform

An end-to-end trade compliance analytics platform that simulates global supply chain operations, processes shipment and customs data, and generates analytics models for supplier risk assessment and duty exposure analysis.

The project demonstrates a complete data workflow:

**Data Generation → ETL Pipeline → Data Warehouse → Analytics Layer → Business Insights**

---

## Overview

Global trade operations require visibility into supplier compliance, customs costs, and shipment performance. This platform simulates a trade compliance environment and provides analytics capabilities for monitoring operational risk.

The platform:

- Generates synthetic supplier, product, shipment, customs, and inspection data
- Ingests data through modular Python ETL pipelines
- Stores operational data in PostgreSQL
- Creates SQL-based analytics models
- Calculates supplier risk scores
- Produces executive-level compliance metrics

---

# Architecture

                Synthetic Data Generation
                          |
                          v
                Python ETL Pipeline
                          |
                          v
                PostgreSQL Data Warehouse
                          |
                          v
                SQL Analytics Layer
                          |
                          v
                Dashboard / BI Reporting


---

# Technology Stack

## Data Engineering

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker

## Analytics

- SQL Views
- Supplier Risk Scoring
- Trade Cost Analysis
- Compliance Metrics

## Platform Components

- Apache Airflow (orchestration framework)
- dbt (transformation framework)
- Apache Spark (future distributed processing)
- Power BI (dashboard layer)

---

# Data Model

The platform uses a relational warehouse model:
suppliers
|
|
shipments -------- products
|
|
+-------- customs_entries
|
|
+-------- inspections


---

---

# ETL Pipeline

The ingestion pipeline processes:

### Supplier Data

Generates supplier profiles including:

- supplier name
- country
- compliance risk rating

### Product Data

Generates:

- product categories
- HTS codes
- product values

### Shipment Data

Tracks:

- supplier relationships
- product movement
- shipment status
- quantities

### Compliance Data

Processes:

- customs declarations
- duty amounts
- inspection outcomes

---

# Analytics Features

## Supplier Risk Scoring

Identifies suppliers requiring compliance review using:

- inspection failure rates
- duty exposure
- supplier risk classification

Example output:

| Supplier | Risk Score | Category |
|---|---:|---|
| Supplier A | 69.46 | High |
| Supplier B | 58.95 | Medium |

---

## Customs Duty Analytics

Analyzes trade costs across:

- countries
- product categories
- shipment activity

Metrics include:

- declared trade value
- duty exposure
- effective duty rates

---

## Executive Compliance Dashboard Metrics

Provides leadership-level KPIs:

- total shipments
- total trade value
- total duty exposure
- high-risk suppliers
- inspection failure rate

---

# Running the Project

# 1. Start Services

```bash
docker compose up -d

# 2. Install Python Dependencies
pip install -r requirements.txt

# 3. Test Database Connection
python3 -m scripts.test_connection

#4. Run Data Pipeline
python3 -m ingestion.pipeline


# Project Structure
trade-analytics-data-platform/

├── ingestion/        # Python ETL pipelines
├── analytics/        # SQL analytics models
├── docs/             # Documentation
├── dashboard/        # BI dashboards
├── airflow/          # Workflow orchestration
├── dbt/              # Transformation models
├── spark/            # Distributed processing
├── tests/            # Testing
└── docker-compose.yml

# Future Enhancements
Automated Airflow scheduling
dbt transformation models
Power BI executive dashboard
Supplier risk prediction model
Real-time shipment monitoring
Cloud deployment using AWS services
Author

- Aditya Adkar

 MS Information Systems
 Syracuse University