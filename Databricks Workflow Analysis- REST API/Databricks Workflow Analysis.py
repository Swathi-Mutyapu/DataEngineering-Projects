%python
import requests
import pandas as pd
from datetime import datetime

# Get workspace details
workspace_url = spark.conf.get(
    "spark.databricks.workspace.url",
    "<providde your workspace url>"
)
token = <enter your pat token>

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def get_jobs_duration_dataframe() -> pd.DataFrame:
    # Retrieve all jobs
    jobs_url = f"{workspace_url}/api/2.1/jobs/list"
    jobs_resp = requests.get(jobs_url, headers=headers)
    jobs = jobs_resp.json().get("jobs", [])

    results = []

    for job in jobs:
        job_id = job["job_id"]
        job_name = job["settings"]["name"]

        # Retrieve last 20 completed runs for the job
        runs_resp = requests.get(
            f"{workspace_url}/api/2.1/jobs/runs/list",
            headers=headers,
            params={"job_id": job_id, "limit": 20, "completed_only": "true"},
        )
        runs = runs_resp.json().get("runs", [])

        # Calculate durations in minutes
        durations = [
            (run["end_time"] - run["start_time"]) / (1000 * 60)
            for run in runs
            if run.get("start_time") and run.get("end_time")
        ]

        if durations:
            results.append(
                {
                    "Job Name": job_name,
                    "Job ID": job_id,
                    "Average Duration (min)": round(sum(durations) / len(durations), 2),
                    "Min Duration (min)": round(min(durations), 2),
                    "Max Duration (min)": round(max(durations), 2),
                    "Runs Analyzed": len(durations),
                }
            )

    return pd.DataFrame(results)


# Create and display DataFrame
df = get_jobs_duration_dataframe()
display(df)
