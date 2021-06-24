import boto3

s3 = boto3.client('s3')

share_url = s3.generate_presigned_url(ClientMethod="get_object",
                                        ExpiresIn=3600,
                                        Params={"Bucket": "my-bucket-test-sdk12-12-31-2", "Key": "bucket.py"})

print(share_url)

# The Key value is one object inside the bucket