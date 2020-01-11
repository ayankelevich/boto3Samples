import boto3
from pprint import pprint

# Plug in your instance id here
instance_id = 'i-081571aadebf49f2c'

aws_con = boto3.session.Session()
ec2_con_re = aws_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_con.client(service_name="ec2", region_name="us-east-1")
pprint(ec2_con_cli.waiter_names)

# client
print("Starting ec2 instance {}".format(instance_id))
ec2_con_cli.start_instances(InstanceIds=[instance_id])
waiter_running = ec2_con_cli.get_waiter('instance_running')
waiter_running.wait(InstanceIds=[instance_id])  # 40 checks after every 15 sec.
print("Now your ec2 instance is up and running")

print("Stopping ec2 instance {}".format(instance_id))
ec2_con_cli.stop_instances(InstanceIds=[instance_id])
waiter_stopped = ec2_con_cli.get_waiter('instance_stopped')  # 40 checks after every 5 sec.
waiter_stopped.wait(InstanceIds=[instance_id])

# resource
my_inst_ob = ec2_con_re.Instance(instance_id)
print("Starting ec2 instance {}".format(instance_id))
my_inst_ob.start()
my_inst_ob.wait_until_running()  # client waiter can also be attached
print("Now your ec2 instance is up and running again")

print("Stopping ec2 instance {}".format(instance_id))
ec2_con_cli.stop_instances(InstanceIds=[instance_id])
waiter_stopped.wait(InstanceIds=[instance_id])
