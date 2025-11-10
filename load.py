import os
import sys
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

try:
    try:
        s3_client.list_objects_v2(Bucket = bucket)
    except:
        print('Access denyed')
        sys.exit(1)   
    dir = 'data'
    file = [f for f in os.listdir(dir) if f.endswith('.json')]
    if len(file)>0:
        filename = dir + '/' +file[0]
        s3filename = file[0]
        s3_client.upload_file(filename, bucket, s3filename)
        os.remove(filename)
    else:
        print('No files to Upload')
except Exception as e: 
    print(e)
    raise e