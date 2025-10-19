💤 Sleep Health ETL Pipeline using AWS Glue
📘 Project Overview

This project demonstrates how to build an **end-to-end ETL (Extract, Transform, Load) data pipeline** using **AWS Glue**, **S3**, and **Athena**.
It processes the **Sleep Health and Lifestyle dataset**, performs cleaning and transformation, and outputs optimized data for analysis.

🧱 Architecture Flow

1. **Amazon S3** stores raw CSV data and processed Parquet files.
2. **AWS Glue Crawler** automatically detects schema and creates metadata in the Glue Data Catalog.
3. AWS Glue ETL Job** performs data cleaning and transformation using PySpark.
4. Amazon Athena** queries and analyzes the processed data directly from S3.

⚙️ AWS Services Used

* Amazon S3 – Data storage for raw and processed files
* **AWS Glue Crawler** – Schema discovery and catalog creation
* **AWS Glue Job** – ETL transformation process
* **AWS IAM** – Access and permission management
* **Amazon Athena** – Query engine for transformed data

🪜 Step-by-Step Implementation
Step 1: Upload Data to S3

* Create an S3 bucket (e.g., `sleep-etl-project-mitesh`).
* Inside the bucket, create two folders:

  * `raw/` → contains the original CSV file (`Sleep_health_and_lifestyle_dataset.csv`)
  * `processed/` → will store the transformed output files

 Step 2: Create AWS Glue Database

* In the AWS Glue Console, create a new database named `sleep_health_db`.
* This database will store metadata from the crawler and ETL job.

 Step 3: Create and Run Glue Crawler

* Name the crawler (e.g., `sleep_health_crawler`).
* Choose **S3** as the data source and set the path to:
  `s3://sleep-etl-project-mitesh/raw/`
* Assign an IAM role with S3 read permissions.
* Choose the target database: `sleep_health_db`.
* Run the crawler to automatically create a table from the CSV file.

Step 4: Create AWS Glue ETL Job

* Go to **AWS Glue → Jobs → Add Job**.
* Name the job `sleep_health_etl_job`.
* Select the same IAM role as the crawler.
* Set the data source to the table created by the crawler.
* Define the data target as `s3://sleep-etl-project-mitesh/processed/` in Parquet format.
* Add and run the ETL script (PySpark) to clean and transform the dataset.

Step 5: Verify Processed Data

* After the job completes, open S3 and check the `processed/` folder.
* You should see output files in **Parquet** format.
* These files are now optimized for analytical queries.

 Step 6: Query Data using Amazon Athena

* Open **Amazon Athena** in the AWS console.
* Create a table pointing to your processed S3 path.
* Run SQL queries to analyze relationships between lifestyle factors and sleep patterns.

📈 Outcome

* Raw CSV data converted into clean, structured Parquet files.
* Faster query performance using Athena.
* Automated, serverless data pipeline fully managed on AWS.

💡 Future Enhancements

* Automate the pipeline using AWS Lambda and EventBridge triggers.
* Integrate AWS QuickSight for dashboard visualization.
* Add Glue Studio visual workflows for easier pipeline orchestration.

👨‍💻 Author

Mitesh Patel
🔗 [GitHub Profile](https://github.com/)
🔗 [LinkedIn Profile](https://www.linkedin.com/)


                
                +-------------------+
                |    S3 Bucket      |
                |  (Raw Data)       |
                | sleep-etl-project |
                +---------+---------+
                          |
                          v
                +-------------------+
                | AWS Glue Crawler  |
                |  (Schema detect)  |
                +---------+---------+
                          |
                          v
                +-------------------+
                | AWS Glue Job      |
                |  (PySpark ETL)    |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   S3 (Processed)  |
                |   Parquet Files   |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Amazon Athena     |
                | Query & Analysis  |
                +-------------------+
