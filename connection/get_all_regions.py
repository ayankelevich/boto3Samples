import boto3

ec2_service_client = boto3.client(service_name='ec2')
for region in ec2_service_client.describe_regions()['Regions']:
    print(region['RegionName'], region['Endpoint'])
    # Create client for every region
    ec2_regional_client = boto3.client(service_name='ec2', region_name=region['RegionName'])

    print(bool([]), len([]), bool([1]), bool(None), bool({}))
