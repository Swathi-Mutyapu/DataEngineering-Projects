🧪 Databricks Delta Lake Schema Evolution with Monthly Snapshots

This repository demonstrates how to manage **schema evolution** in Delta Lake while maintaining **monthly snapshot tables** based on daily source data. It's a real-world inspired data engineering project using PySpark and Databricks.

## 📘 Business Context

We work with a **daily Delta table** that gets overwritten every day. On the **1st of every month**, we need to capture a snapshot of this daily data and save it to a **monthly snapshot table** to track trends over time.

However, there’s a twist — **the schema of the daily source evolves**. This includes:
- Column additions
- Column deletions
- Changes in column data types
- Reordering of columns

If not handled correctly, these schema changes will cause failures or inconsistencies during the monthly snapshot process.

## ✅ Goal

Build a robust snapshot pipeline that:
- **Handles schema changes automatically**
- **Casts mismatched types** to prevent write failures
- **Uses Delta Lake’s schema evolution support**
- Appends snapshots with the correct schema into a monthly Delta table

## 🛠 Tech Stack

| Tool         | Purpose                                 |
|--------------|------------------------------------------|
| Databricks   | Cloud platform and notebook orchestration |
| Delta Lake   | Storage format supporting ACID & evolution |
| PySpark      | Processing and transformation            |
| SQL (Delta)  | Schema management and inspection         |

---

## 📂 Data Tables

| Table Name              | Description                                |
|-------------------------|--------------------------------------------|
| `daily_agg_orders`      | Daily source table (overwritten each day)  |
| `monthly_agg_orders`    | Monthly snapshot table (appended monthly)  |

---

## 🔁 Workflow Overview

1. Read daily data.
2. Add a `Snapshot_date` column.
3. Check if the monthly table exists:
   - If **yes**: Align schema and cast types accordingly.
   - If **no**: Create the table.
4. Append the aligned data using `mergeSchema = true`.

---

## 🧾 Key Scenarios Handled

### 🔹 Scenario 1: Column Added in Daily Source
- Handled by enabling `mergeSchema = true`.
- A new column is automatically added to the monthly table.

### 🔹 Scenario 2: Column Dropped in Daily Source
- Missing column is skipped in write.
- Monthly table retains existing columns and fills nulls for dropped ones.

### 🔹 Scenario 3: Column Data Type Changed
- Example: A field changes from `integer` to `string`.
- We manually cast daily data to match the monthly schema before writing.

### 🔹 Scenario 4: Column Order Changed
- Column alignment logic ensures column positions don’t cause issues.

