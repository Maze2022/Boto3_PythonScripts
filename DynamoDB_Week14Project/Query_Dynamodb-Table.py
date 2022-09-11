import boto3

from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('Sports')
response = table_name.query(
    KeyConditionExpression=Key('Name').eq('Hockey')
)

print("The query returned the item: ")
for item in response['Items']:
    print(item)