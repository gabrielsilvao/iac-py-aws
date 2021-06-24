import boto3
import botocore
import argparse
import os

def create_bucket(args):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=args.name)

def upload_file(args):
    s3 = boto3.client('s3')
    s3.upload_file(args.file, args.name, args.file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create a bucket s3")
    parser.add_argument("-n", "--name", metavar="NAME", help="Name of the bucket")
    parser.add_argument("-f", "--file", metavar="FILE", help="Name of the file")
    parser.add_argument("-s", "--sign-file", metavar="SIGN-FILE", help="Name of the file")
    args = parser.parse_args()
    create_bucket(args)
    upload_file(args)
