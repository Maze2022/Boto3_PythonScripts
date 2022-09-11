import boto3

dynamodb = boto3.resource("dynamodb")
table_name = dynamodb.Table('Sports')
response = table_name.delete_item(
    Key={
        'Name':'Table Tennis',
        'TopPlayer':'Fan Zhendong'
    } 
)

print('The item specified has been deleted')