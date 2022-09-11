import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'TopPlayer',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'TopPlayer',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits':10,
    },
    TableName='Sports',
)

print('Table created')