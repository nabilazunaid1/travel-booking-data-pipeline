# End-to-End Travel Booking Data Engineering Pipeline

## 1. Project Overview

This portfolio project demonstrates the development of an end-to-end data engineering pipeline for a fictional travel booking company.

The pipeline processes synthetic travel booking records, performs data cleaning and validation, and prepares reliable datasets for downstream analytics.

The project is being developed incrementally, beginning with a local Python ETL pipeline and expanding toward PostgreSQL, Google BigQuery, Apache Airflow, Docker, and CI/CD.

## 2. Business Problem

Travel booking platforms collect data from multiple systems. Raw booking data may contain duplicate records, missing fields, invalid amounts, and inconsistent booking information.

Poor data quality can affect financial reporting, customer analytics, and operational decisions.

**Project objective:** Build a reproducible ETL pipeline that transforms raw booking records into clean, validated data suitable for analytics.

## 3. Architecture

Current implementation:

```text
Synthetic Booking Data
         |
         v
data/raw/bookings.csv
         |
         v
Python ETL Pipeline
  | Extract
  | Transform
  | Validate
  | Load
         |
         v
data/processed/clean_bookings.csv
```

Planned architecture:

```text
CSV / JSON / REST API
          |
          v
     Python ETL
          |
          v
     PostgreSQL
          |
          v
   Google BigQuery
          |
          v
     SQL Analytics
```

Planned supporting technologies include Apache Airflow for orchestration, Docker for containerization, and GitHub Actions for CI/CD.

## 4. Technology Stack

| Technology | Purpose | Status |
|---|---|---|
| Python 3.12 | Data processing | Implemented |
| pandas | Data cleaning and transformation | Implemented |
| unittest | Automated unit testing | Implemented |
| Git | Version control | In progress |
| PostgreSQL | Relational database | Planned |
| Google BigQuery | Analytics warehouse | Planned |
| Apache Airflow | Pipeline scheduling | Planned |
| Docker | Containerization | Planned |
| GitHub Actions | CI/CD | Planned |

## 5. Project Structure

```text
Travel Booking Pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   └── etl_pipeline.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

Generated datasets and local virtual environments are excluded from Git.

## 6. Data Quality Rules

The pipeline performs the following checks:

1. Validates the expected CSV columns.
2. Removes duplicate booking IDs, keeping the first occurrence.
3. Rejects records with missing required values.
4. Rejects invalid booking or travel dates.
5. Rejects travel dates earlier than booking dates.
6. Rejects booking amounts that are not positive.
7. Accepts only Confirmed, Pending, and Cancelled booking statuses.

## 7. Sample Pipeline Results

| Metric | Result |
|---|---:|
| Raw booking records | 11 |
| Duplicate records removed | 1 |
| Invalid records rejected | 2 |
| Valid output records | 8 |

All data is synthetic and intended for demonstration purposes.

## 8. Run the Project Locally

### Prerequisites

- Python 3.12
- Git
- VS Code or another code editor

### Create a virtual environment

```powershell
python -m venv .venv
```

### Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Generate the sample dataset

```powershell
.\.venv\Scripts\python.exe src/generate_data.py
```

### Run the ETL pipeline

```powershell
.\.venv\Scripts\python.exe src/etl_pipeline.py
```

### Run automated tests

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Expected result:

```text
Ran 6 tests

OK
```

## 9. Current Implementation

- [x] Project setup
- [x] Synthetic CSV data generation
- [x] Python ETL pipeline
- [x] Duplicate removal and data validation
- [x] Logging
- [x] Six automated unit tests
- [ ] Publish GitHub repository
- [ ] Multi-source data ingestion
- [ ] PostgreSQL integration
- [ ] BigQuery data warehouse
- [ ] Star schema data modeling
- [ ] Airflow scheduling
- [ ] Docker containerization
- [ ] GitHub Actions CI/CD
- [ ] SQL analytics

## 10. Future Analytics

The completed platform will support questions such as:

- How many bookings were confirmed or cancelled?
- What is the total value of confirmed bookings?
- Which destinations are most popular?
- How does booking activity change over time?
- Which customers book most frequently?

## 11. Data Privacy

All records used in this project are synthetic. No real customer information or company data is required.
