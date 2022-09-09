# CREATE VPC
import boto3

#resource =  boto3.client("ec2")
#response = resource.create_vpc(CidrBlock= '10.0.0.0/20')
#print(response)

##################################
#DESCRIBE VPC - All VPC's in your account
resource = boto3.client("ec2")
response = resource.describe_vpcs()
no_of_vpcs = response["Vpcs"]
print(response)
print(len(no_of_vpcs))

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
