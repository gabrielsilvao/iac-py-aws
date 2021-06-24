import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucket-test-sdk12-12-31-2')
