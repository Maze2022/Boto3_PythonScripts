import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

data = response["Reservations"]
for instance  in data:
    instance=instance["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        print(instance_id)