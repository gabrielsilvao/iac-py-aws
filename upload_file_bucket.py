import boto3

s3 = boto3.client('s3')

filename = 'bucket.py'
bucket_name = 'my-bucket-test-sdk12-12-31-2'

s3.upload_file(filename, bucket_name, filename)
