# Databricks Jobs Runtime Analyzer 📊

This project analyzes **Databricks job execution durations** by calling the Databricks Jobs REST API and producing a **summary DataFrame** with average, minimum, and maximum runtimes per job.

It helps data engineers and platform teams gain visibility into job performance, identify long-running jobs, and support cost and SLA monitoring initiatives.

---

## 🚀 What This Project Does

For each Databricks job in a workspace, the script:

- Fetches all jobs using the Databricks Jobs REST API
- Retrieves the **last 20 completed runs** for each job
- Calculates:
  - Average runtime (minutes)
  - Minimum runtime (minutes)
  - Maximum runtime (minutes)
  - Number of runs analyzed
- Displays the results as a Pandas DataFrame inside a Databricks notebook

---

## 📊 Sample Output

| Job Name | Job ID | Average Duration (min) | Min Duration (min) | Max Duration (min) | Runs Analyzed |
|--------|--------|------------------------|--------------------|--------------------|---------------|
| Daily Ingest | 123 | 14.6 | 12.3 | 19.8 | 20 |
| Gold Refresh | 456 | 42.1 | 38.7 | 49.2 | 18 |

---

## 🏗️ Architecture Overview
Databricks Notebook
->
Databricks Jobs REST API
->
Job Runs Metadata (JSON)
->
Python Processing
->
Pandas DataFrame
->
Notebook Display


---

## 🔧 Prerequisites

- Access to a Databricks workspace
- Databricks Personal Access Token (PAT)
- Python-enabled Databricks notebook
- Permissions to:
  - List jobs
  - List job runs

---

## 🔐 Authentication

Authentication is handled using a **Databricks Personal Access Token (PAT)**.

```python
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
