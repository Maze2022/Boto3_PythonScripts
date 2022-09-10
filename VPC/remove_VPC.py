import boto3

vpc = boto3.client('ec2')
response = vpc.delete_vpc(
    VpcId='vpc-085ae586c69f59502'

)
print('vpc deleted')

