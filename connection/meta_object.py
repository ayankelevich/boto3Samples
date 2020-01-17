# Allows to use client methods from a resource connection

import boto3
aws_session = boto3.session.Session()
ec2_resource = aws_session.resource(service_name="ec2")

for x in dir(ec2_resource):
    if "meta" in x:
        print(x)

l11 = list(filter(lambda elem: 'meta' in elem, dir(ec2_resource)))
print(l11)

#  no_spam_2 = [meal if "spam" not in meal else "skpipped" for meal in menu]

print(dir(ec2_resource))
print(dir(ec2_resource.meta))

for each_item in ec2_resource.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])