import boto3

share_url = s3.generate_presigned_url(ClientMethod="get_object",
                                        ExpiresIn=3600,
                                        Params={"Bucket": "my-bucket-test-sdk12-12-31-2", "key": "create_bucket.py"})

print(share_url)
