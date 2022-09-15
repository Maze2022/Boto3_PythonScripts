#Week15 - SQS_QueueUrl

import boto3

sqs = boto3.client('sqs')

response = sqs.get_queue_url(
    QueueName='Lambda-queue'
    )

url = response['QueueUrl']

print(url)