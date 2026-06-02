# Mutual Fund Analytics Project

## Day 1 – Data Ingestion & ETL

### Tasks Completed

* Created project folder structure.
* Loaded all provided CSV datasets using Pandas.
* Inspected dataset shapes, data types, and sample records.
* Fetched live NAV data from mfapi.in.
* Retrieved NAV history for six mutual fund schemes.
* Performed AMFI code validation between fund_master and nav_history datasets.
* Conducted initial data quality assessment.

### Key Findings

* Total schemes in fund_master: 40
* Unique fund houses: 10
* Categories identified: Equity, Debt
* Risk categories identified: Low, Moderate, Moderately High, High, Very High
* Missing AMFI codes: 0
* All AMFI codes from fund_master were found in nav_history.

### Deliverables

* data_ingestion.py
* live_nav_fetch.py
* requirements.txt
* README.md
