import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
bucket_name = 'ri79216bucket'
file_name = 'file.txt.rtf'

if not os.path.exists(file_name):
    with open(file_name, 'w') as f:
        f.write("This is a test RTF file uploaded to S3.")

print(f"✅ File '{file_name}' created or found locally.")

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"✅ File '{file_name}' uploaded to bucket '{bucket_name}'")
except ClientError as e:
    print(f"❌ Upload failed: {e}")

