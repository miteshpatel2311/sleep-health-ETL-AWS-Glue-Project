import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Catalog
input_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="sleep_health_db",
    table_name="sleep_health_and_lifestyle_dataset",
    transformation_ctx="input_dynamic_frame"
)

# Convert to Spark DataFrame for transformations
df = input_dynamic_frame.toDF()

# Clean and Transform
df = df.select([col(c).alias(c.lower()) for c in df.columns])
df = df.filter(col("age").isNotNull())
df = df.withColumn("sleep_duration", col("sleep_duration").cast("float"))

# Convert back to DynamicFrame
output_dynamic_frame = glueContext.create_dynamic_frame.from_dataframe(df, glueContext, "output_dynamic_frame")

# Write as Parquet to S3
glueContext.write_dynamic_frame.from_options(
    frame=output_dynamic_frame,
    connection_type="s3",
    connection_options={"path": "s3://sleep-etl-project-mitesh/processed/"},
    format="parquet",
    transformation_ctx="output_dynamic_frame"
)

job.commit()
