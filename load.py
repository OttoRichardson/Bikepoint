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
        # Test if we have access to the bucket
        s3_client.list_objects_v2(Bucket = bucket)
    except:
        print('Access denyed')
        sys.exit(1)   
    dir = 'data'
    # Get a list of JSON files in the directory
    file = [f for f in os.listdir(dir) if f.endswith('.json')]
    
    if len(file)>0: # checks if there is a file to upload
        filename = dir + '/' +file[0]
        s3filename = file[0]         # Take the first JSON file
        s3_client.upload_file(filename, bucket, s3filename) # Upload the file to the specified S3 bucket
        os.remove(filename) # Remove the file locally after successful upload
    else:
        print('No files to Upload')
except Exception as e: 
    print(e)
    raise e    # Catch any unexpected exceptions and print the error