import sys
import botocore     # not needed if you references exceptions as boto3.exception.botocore.exception

# import boto3333    # test to get exception name

try:
    import boto3
except ModuleNotFoundError as e:     # Python exception, not boto3
    print("how do I know the name of the exception? (see comment below)")
    print(e)
    sys.exit(1)   # no reason to continue, if boto3 is not installed
except Exception as e:
    print(e)

# To find the actual exception name, like ModuleNotFoundError, do not intercept it with try:except and see the error

print(dir(boto3.exceptions))
print(dir(boto3.exceptions.botocore.exceptions))
# print(dir(botocore.exceptions))

try:
    my_session = boto3.session.Session(profile_name='bogus')
except botocore.exceptions.ProfileNotFound as e:
    print(e)
    print(dir(e))    # does not have response object as shown in next example
    sys.exit(2)   # no reason to continue, if boto3 is not installed


try:
    iam_console_resource = my_session.resource(service_name='iam')
    for user in iam_console_resource.users.all():
        print(user)
except botocore.exceptions.ClientError as e:
    print(e)
    print(e.response)
    print(dir(e))     # has response object
    print(e.response['Error'])
    print(e.response['Error']['Code'])
    sys.exit(2)
