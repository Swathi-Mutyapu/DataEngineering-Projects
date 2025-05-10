  
# Real-Time Crypto Price Streaming using Databricks

This project demonstrates how to build a fault-tolerant, real-time data pipeline to track cryptocurrency prices using Spark Structured Streaming in Databricks Community Edition. It simulates streaming by ingesting JSON files into DBFS and processes them incrementally with schema enforcement and checkpointing enabled.

## 🔧 Tech Stack

- **Apache Spark Structured Streaming**
- **Databricks Community Edition**
- **Python**
- **DBFS (Databricks File System)**
- **Delta Lake**

## 📂 File Structure

- `Real-Time_Crypto_Price_Tracker_Using_Databricks.dbc` – Databricks notebook archive that contains all the code and markdown needed to run the project.

## 💡 Key Concepts Covered

- Structured Streaming from DBFS using JSON files  
- Schema enforcement to handle fragile streaming schemas  
- Fault tolerance with checkpointing  
- Incremental processing for efficient streaming  
- Writing data into Delta Tables  
- Temporary vs Managed tables in Spark SQL

## 🚀 How to Use

1. **Log in to [Databricks Community Edition](https://community.cloud.databricks.com/).**
2. Go to **Workspace > Import** and upload `Real-Time_Crypto_Price_Tracker_Using_Databricks.dbc`.
3. Open the notebook and run each cell step-by-step.
4. Make sure to create folders in DBFS that match those used in the config:
   - `dbfs:/FileStore/crypto_stream/`
   - `dbfs:/FileStore/crypto-checkpoints/`
   - `dbfs:/FileStore/crypto-output/`

## 📸 Blog

A complete write-up with real human insights, annotated screenshots, and architecture diagrams is available [here](https://gerbil-purple-7gfl.squarespace.com/config/pages/68009c952c57e938cc907b3e)

## ⚠️ Limitations

- This project uses DBFS for streaming simulation, which works well for demos but isn’t recommended for production. For real-time ingestion, tools like Kafka or Databricks Auto Loader are more suitable.
