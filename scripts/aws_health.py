
import boto3

# Create an EC2 client
ec2 = boto3.client("ec2")

# Retrieve EC2 instance information
response = ec2.describe_instances()

print("=" * 45)
print("       AWS EC2 HEALTH MONITOR")
print("=" * 45)

# Process reservations
for reservation in response["Reservations"]:

    for instance in reservation["Instances"]:

        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]
        instance_state = instance["State"]["Name"]

        print(f"\nInstance ID: {instance_id}")
        print(f"Instance Type: {instance_type}")
        print(f"Instance State: {instance_state}")

print("\nAWS EC2 monitoring completed")
