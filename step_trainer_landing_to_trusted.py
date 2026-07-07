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
job.init("step_trainer_landing_to_trusted")

step_landing_node = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://stedi-ronit-1470/step_trainer/landing/"]}
)
step_landing_df = step_landing_node.toDF()
customer_curated_df = spark.read.json("s3://stedi-ronit-1470/customer/curated/")

joined_df = step_landing_df.join(
    customer_curated_df,
    step_landing_df["serialNumber"] == customer_curated_df["serialNumber"],
    "inner"
)

step_trusted_df = joined_df.select(step_landing_df["*"])
step_trusted_df.write.mode("overwrite").json("s3://stedi-ronit-1470/step_trainer/trusted/")
job.commit()
