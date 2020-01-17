import boto3
import datetime

aws_mag_con = boto3.session.Session()
ec2_con_re = aws_mag_con.resource(service_name="ec2", region_name="us-east-1")

sts_con_cli = aws_mag_con.client(service_name="sts", region_name="us-east-1")
response = sts_con_cli.get_caller_identity()
print(response['Account'], response.get('Account'))
my_own_id = response.get('Account')

today = datetime.datetime.now()
# checking_start_time = str(datetime.datetime(today.year, today.month, today.day, 18, 18, 58))
# make datetime of the snapshot for testing
checking_start_time = str(datetime.datetime(2019, 7, 16, 18, 18, 58))
print(checking_start_time)

for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S") == checking_start_time:
        print(each_snap, each_snap.id, each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))
