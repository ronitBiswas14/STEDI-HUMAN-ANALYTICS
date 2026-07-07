CREATE EXTERNAL TABLE IF NOT EXISTS customer_trusted (
    `customerName` string,
    `email` string,
    `phone` string,
    `serialNumber` string,
    `shareWithResearchAsOfDate` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stedi-ronit-1470/customer/trusted/'
TBLPROPERTIES ('classification'='json');
