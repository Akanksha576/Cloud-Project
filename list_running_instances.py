import boto3

# Create EC2 client with region specified
ec2 = boto3.client('ec2', region_name='us-east-1')  

# Get only 'running' instances
response = ec2.describe_instances(
    Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
)

print("✅ Running EC2 Instances:")

# Loop through all reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        public_ip = instance.get('PublicIpAddress', 'N/A')
        print(f" - ID: {instance_id}, Type: {instance_type}, Public IP: {public_ip}")
