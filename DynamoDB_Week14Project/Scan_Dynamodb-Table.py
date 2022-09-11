#import boto3
#dynamodb = boto3.resource('dynamodb')
#table_name = dynamodb.Table('Sports')
#response = table_name.scan()
#print(response)

#from boto3.dynamodb.conditions import Key, Attr
#dynamodb = boto3.resource('dynamodb')
#table_name = dynamodb.Table('Sports')
#response = table_name.scan(
    #FilterExpression=Attr('TopPlayer').eq('Giannis Antetokounmpo')
#)
#print(response)

import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('Sports')
response = table_name.scan(
    FilterExpression=Attr('Name').begins_with('T')
)
print(response)