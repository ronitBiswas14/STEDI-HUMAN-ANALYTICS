CREATE EXTERNAL TABLE IF NOT EXISTS customer_landing (
    `customerName` string,
    `email` string,
    `phone` string,
    `serialNumber` string,
    `shareWithResearchAsOfDate` bigint,
    `shareWithPublicAsOfDate` bigint,
    `shareWithFriendsAsOfDate` bigint,
    `birthday` string,
    `registrationDate` bigint,
    `lastUpdateDate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-ronit-1470/accelerometer/landing/'
TBLPROPERTIES ('classification'='json');
