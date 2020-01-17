#!/Users/alex/venv_boto3/bin/python

# the line above plus chmod + x allows executing it by itself without using python3 ec2connection.py

import boto3
# for beautified JSON print
from pprint import pprint

iam_console_client = boto3.client('iam')

users = iam_console_client.list_users()

print(users['Users'])

# Print list example (heavy-handed)
user_names = list(map(lambda x: x['UserName'], users['Users']))
print(user_names)
# Get names
for x in users['Users']:
    print(x['UserName'])

ec2_console_client = boto3.client('ec2')
ec2s = ec2_console_client.describe_instances()
# for beautified JSON print
pprint(ec2s)

# does not work <===================
s3_console_resource = boto3.resource('s3')
filters = [{'Name': 'name', 'Values': ['12chairs.com']}]
bucket_list_filtered = s3_console_resource.buckets.filter(Filter=filters)
for bucket in bucket_list_filtered:
    print(bucket.name, bucket.creation_date)

sts_console_client = boto3.client('sts')
response = sts_console_client.get_caller_identity()
print(response['UserId'], response['Account'], response['Arn'])

# Example of using client
# ec2_con_cli.start_instances(InstanceIds=[instance_id])