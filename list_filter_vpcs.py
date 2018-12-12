import boto3

client = boto3.client('ec2',region_name='us-east-1')
response = client.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                '<Enter you VPC name here>',
            ]
        },
        {
            'Name': 'cidr-block-association.cidr-block',
            'Values': [
                '10.0.0.0/16', #Enter you cidr block here
            ]
        },
    ]
)
resp = response['Vpcs']
if resp:
    print(resp)
else:
    print('No vpcs found')