import boto3

dynamodb = boto3.client('dynamodb')

#table_name = dynamodb.Table('Sports')

response = dynamodb.delete_table(
    TableName='Sports',
)

print("The Sports table has been successfully deleted")