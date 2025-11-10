import os
from dotenv import load_dotenv
import boto3


load_dotenv()

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket = os.getenv('Bucket')

#print(bucket)

s3_client = boto3.client(
    's3'
    , aws_access_key_id = aws_access_key
    , aws_secret_access_key = aws_secret_key
)

filename = 'data/2025-11-10T09-51-07.json'
s3filename = '2025-11-10T09-51-07.json'

s3_client.upload_file(filename, bucket, s3filename)