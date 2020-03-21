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

# name filter does NOT work, probably just for objects in bucket <===================
s3_console_resource = boto3.resource('s3')
filter1 = {"Name": "name", "Values": ["12chairs.com", "bytemple.com"]}
filter2 = {"Name": "tag:Env", "Values": ["TestInstance", "testinstance"]}

bucket_list_filtered = s3_console_resource.buckets.filter(Filter=[filter1])
for bucket in bucket_list_filtered:
    print(bucket.name, bucket.creation_date)



s3_console_client = boto3.client('s3')
s3_console_client.put_bucket_tagging(
    Bucket='lab2-input-bucket-ay',
    Tagging={'TagSet': [{'Key': 'tag_key', 'Value': 'tag_value123'}]}
)

# s3_console_client.delete_bucket_tagging(
#     Bucket='lab2-input-bucket-ay'
# )

# for other objects, Object name goes into the Resources list
ec2_console_client.create_tags(Resources=['snap-0a27b3cc04cb78ad1'], Tags=[{'Key': 'backup', 'Value': 'yes/no'}])
# ec2_console_client.delete_tags(Resources=['snap-0a27b3cc04cb78ad1'], Tags=[{'Key': 'backup', 'Value': 'yes'}])

# Example of using client
# ec2_con_cli.start_instances(InstanceIds=[instance_id])