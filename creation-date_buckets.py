#Date creation of Buckets

import boto3

resource = boto3.client('s3')
response_creation_date = resource.list_buckets()["Buckets"][2]["CreationDate"]

response_creation_date.strftime("%d%m%y_%H:%M:%S")

for bucket in resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])

