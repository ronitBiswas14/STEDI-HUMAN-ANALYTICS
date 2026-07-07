CREATE EXTERNAL TABLE IF NOT EXISTS accelerometer_landing (
    `user` string,
    `timestamp` bigint,
    `x` double,
    `y` double,
    `z` double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-ronit-1470/accelerometer/landing/'
TBLPROPERTIES ('classification'='json');
