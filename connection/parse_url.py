import boto3
import urllib.parse


s3_service_client = boto3.client('s3')
for bucket in s3_service_client.list_buckets()['Buckets']:
    print(bucket['Name'])


print(urllib.parse.unquote_plus('s3://bucket_name/folder%241/file1.txt+fil32.txt'))

print(urllib.parse.unquote_plus('campaign%3DvSphere%207.0'))

# print(urllib.parse.unquote("https://website/folder%241?file1.txt"))

print(urllib.parse.urlparse("https://website/folder%241?file1.txt")[2])
