CREATE EXTERNAL TABLE IF NOT EXISTS accelerometer_trusted (
    `user` string,
    `timestamp` bigint,
    `x` double,
    `y` double,
    `z` double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-ronit-1470/accelerometer/trusted/'
TBLPROPERTIES ('classification'='json');

