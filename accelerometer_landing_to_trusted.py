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
job.init("accelerometer_landing_to_trusted")

accel_node = glueContext.create_dynamic_frame.from_options(
    connection_type="s3", 
    format="json",
    connection_options={"paths": ["s3://stedi-ronit-1470/accelerometer/landing/"]},
)
accel_df = accel_node.toDF()
customer_trusted_df = spark.read.json("s3://stedi-ronit-1470/customer/trusted/")

joined_df = accel_df.join(
    customer_trusted_df,
    (accel_df["user"] == customer_trusted_df["email"]) & 
    (accel_df["timestamp"] >= customer_trusted_df["shareWithResearchAsOfDate"]),
    "inner"
)

accel_trusted_df = joined_df.select(accel_df["*"])
accel_trusted_df.write.mode("overwrite").json("s3://stedi-ronit-1470/accelerometer/trusted/")
job.commit()
