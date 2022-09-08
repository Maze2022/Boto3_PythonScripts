# List S3 Buckets

#METHOD 1
import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = response["Buckets"] #The brackets [] is used to access the elements of 'response'
for bucket in buckets:
    print(bucket["Name"])
    
#METHOD 2
import boto3
resource = boto3.resource('s3')
for bucket in resource.buckets.all():
    print(bucket.name)
    