import boto3
import json

lambda_client = boto3.client('lambda', region_name='us-east-1')  # Replace with your region

payload = {
    "Records": [
        {
            "s3": {
                "bucket": {"name": "ri79216bucket"},
                "object": {"key": "file.txt.rtf"}
            }
        }
    ]
}

response = lambda_client.invoke(
    FunctionName='S3UploadLogger',
    InvocationType='RequestResponse',
    Payload=json.dumps(payload),
)

response_payload = response['Payload'].read().decode()
print("✅ Lambda response:")
print(response_payload)
