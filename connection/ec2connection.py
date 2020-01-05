#!/Users/alex/venv_boto3/bin/python

# the line above  plus chmod + x allows executing it by iteself without using python3 ec2connection.py
import boto3

my_session_2 = boto3.session.Session(profile_name='jules')
#
# # if session is not explicitly created, implicit "default" one will be used with [default] profile

print('==== session resources =====')
print(my_session_2.get_available_resources())

# #  RESOURCE: high level, more object "." operations, last is dict?. Not available for all services
# #  CLIENT: low level, more dict operations, first is object?

print('===== ec2 instance ======')
ec2_console_client = my_session_2.client("ec2")
for res in dir(ec2_console_client):
     if "stance" in res:
         print(res)

my_session_1 = boto3.session.Session(region_name='us-west-2')
print('==== session attributes: region, available profiles =======')
print(my_session_1.region_name, my_session_1.available_profiles)

# Only ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
# are available for resources

# Start a new instance and plug in the id for this fragment to work
# ec2_console_resource = my_session_1.resource("ec2")
# my_instance = ec2_console_resource.Instance(id='i-0673c4324e8054a01')
# print('dir(my_instance):', dir(my_instance))
# i_state = my_instance.state
# print(i_state, i_state['Name'], my_instance.classic_address, my_instance.key_pair, my_instance.key_name)

iam_console_resource = my_session_1.resource('iam')
for user in iam_console_resource.users.all():
    print(user)
for user in iam_console_resource.groups.all():
    print(user)

s3_console_resource = my_session_1.resource(service_name='s3')
for i_bucket in s3_console_resource.buckets.all():
    print(i_bucket.name)

#  meta: for resource object get operations from client object

