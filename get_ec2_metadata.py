import requests

base_url = "http://169.254.169.254/latest/meta-data/"
keys = [
    "instance-id",
    "ami-id",
    "hostname",
    "public-ipv4",
    "local-ipv4",
    "security-groups"
]

print(" EC2 Instance Metadata:")
for key in keys:
    try:
        response = requests.get(base_url + key, timeout=2)
        print(f"{key}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"{key}: Failed to retrieve ({e})")
