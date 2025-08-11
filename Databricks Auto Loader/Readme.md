# Databricks – Auto Loader

## 📌 What is Auto Loader?

Auto Loader in Databricks is a **Structured Streaming** feature that simplifies and optimizes the ingestion of new data files as they arrive in cloud storage (S3, ADLS, Volumes, or GCS) into **Delta Lake** tables.

It automatically detects and processes only the files that haven’t been ingested before — a process known as **incremental ingestion**.

---

## ✨ Key Features

1. **Incremental File Ingestion** – Detects and processes only new files, supporting exactly-once processing when writing to Delta tables.  
2. **Streaming and Batch Modes** – Works for both real-time pipelines and historical/batch loads, with seamless switching.  
3. **Schema Inference and Evolution** – Infers schema automatically, stores it in `cloudFiles.schemaLocation`, and supports automatic schema evolution.  
4. **Checkpointing for State Management** – Acts as a bookmark, remembering which files have been read, the last record processed, and the schema used.

---

## 🛠 Hands-On Example Using Volumes

For this demo, we’ll use **Databricks Volumes** instead of S3, GCS, or ADLS, as they are easier to use in a demonstration and do not require external credentials.

---

### **Step 1 – Create an Input Folder**
Inside a Volume, create an input folder with **date-based subfolders** (e.g., `/2025/08/01/`). This structure simulates real-world pipelines where files arrive daily in partitioned folders.

---

### **Step 2 – Simulate Data Arrival**
Since we are not connected to external systems in this demo, manually add CSV files either by:
- Saving with `pandas.to_csv()` in Databricks.
- Uploading directly through the Databricks UI.  
In production, these files would arrive automatically from upstream systems.

---

### **Step 3 – Set Schema & Checkpoint Paths**
Define:
- **Schema path** – Where the inferred schema will be stored.
- **Checkpoint path** – Where Auto Loader saves ingestion state to ensure exactly-once processing.  

For small demos, these can be the same path. For production, they are often kept separate for better operational control.

---

### **Step 4 – Configure Auto Loader to Read Files**
Configure `spark.readStream` to use the **cloudFiles** format with the desired file type (CSV in this case). Enable recursive scanning of subdirectories and use file pattern filters (e.g., `*.csv`) to process only relevant files. Schema hints can be applied to enforce data types on specific columns.

---

### **Step 5 – Write Data to a Delta Table**
Use `writeStream` to write the streaming DataFrame into a Delta table. Set the output mode to `append` and use the same checkpoint location to ensure fault tolerance and prevent reprocessing of files. If schema hints were set earlier, the written data will reflect those types.

---

### **Step 6 – Simulate Streaming**
To test incremental ingestion, add new CSV files into date-based subfolders. Auto Loader will detect only these new files (based on checkpoint metadata) and ingest them into the Delta table without reprocessing already ingested files.

Example:  
If `/2025/08/04/` and `/2025/08/05/` have already been processed, adding files to `/2025/08/06/` will result in only the new day’s data being ingested.

---

## 🏁 Summary

Auto Loader:
- Simplifies incremental ingestion into Delta tables.
- Supports streaming and batch pipelines.
- Handles schema evolution, checkpointing, and scalable file detection.
- Scales from simple demonstrations to enterprise-grade ingestion pipelines.
