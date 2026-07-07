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
job.init("machine_learning_curated")

step_trusted_df = spark.read.json("s3://stedi-ronit-1470/step_trainer/trusted/")
accel_trusted_df = spark.read.json("s3://stedi-ronit-1470/accelerometer/trusted/")

joined_df = step_trusted_df.join(
    accel_trusted_df,
    step_trusted_df["sensorReadingTime"] == accel_trusted_df["timestamp"],
    "inner"
)

ml_curated_df = joined_df.drop("user")
ml_curated_df.write.mode("overwrite").json("s3://stedi-ronit-1470>/machine_learning/curated/")
job.commit()
