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
job.init("customer_trusted_to_curated")

customer_trusted_df = spark.read.json("s3://stedi-ronit-1470/customer/trusted/")
accel_trusted_df = spark.read.json("s3://stedi-ronit-1470/accelerometer/trusted/")

joined_df = customer_trusted_df.join(
    accel_trusted_df,
    customer_trusted_df["email"] == accel_trusted_df["user"],
    "inner"
)

customer_curated_df = joined_df.select(customer_trusted_df["*"]).distinct()
customer_curated_df.write.mode("overwrite").json("s3://stedi-ronit-1470/customer/curated/")
job.commit()
