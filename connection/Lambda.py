# Possible, although clearly not good, method of authentication
# my_session = boto3.session.Session(aws_access_key_id = "...", aws_secret_access_key_id = "...")
# use Use Existing Role dropdown.  You won't need to create my_session, just the console

# Create client with a default session
import boto3
import my_utils

ec2_client = boto3.client(service_name='ec2', region_name='us-east-1')
print(my_utils.filtered_list_filter('snap', dir(ec2_client)))
