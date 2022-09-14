#Week15 - SQS_Queue

import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='Lambda-queue'
    )
    
print('Queue created')