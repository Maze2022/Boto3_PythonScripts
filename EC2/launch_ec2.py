import boto3

ec2 = boto3.client("ec2")
response = ec2.run_instances(ImageId="ami-0c2ab3b8efb09f272",
                              InstanceType="t2.micro",
                              MaxCount=2,
                              MinCount=1
                              )

print(response)

