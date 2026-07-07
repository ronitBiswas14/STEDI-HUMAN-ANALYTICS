CREATE EXTERNAL TABLE IF NOT EXISTS machine_learning_curated (
    `sensorReadingTime` bigint,
    `serialNumber` string,
    `distanceFromObject` int,
    `timestamp` bigint,
    `x` double,
    `y` double,
    `z` double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-ronit-1470/step_trainer/curated/'
TBLPROPERTIES ('classification'='json');

