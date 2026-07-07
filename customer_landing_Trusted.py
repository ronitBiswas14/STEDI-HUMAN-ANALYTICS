import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("customer_landing_to_trusted")

# Read from Landing Zone
customer_node = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False}, 
    connection_type="s3", 
    format="json",
    connection_options={"paths": ["s3//stedi-ronit-1470/customer/landing/"]}
)
customer_df = customer_node.toDF()

# Filter using a clean SQL-style string to avoid syntax issues
customer_trusted_df = customer_df.filter("shareWithResearchAsOfDate IS NOT NULL")

# Write to Trusted Zone
customer_trusted_df.write.mode("overwrite").json("s3://stedi-ronit-1470/customer/trusted/")
job.commit()
