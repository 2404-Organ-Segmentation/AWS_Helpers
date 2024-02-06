import logging
import boto3
import os
from botocore.exceptions import ClientError


class s3_wrapper:
    def __init__(self):
        self.s3 = boto3.client('s3')
    
    def list_buckets(self):
        response = self.s3.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    
    def create_bucket(self, bucket_name):
        try:
            self.s3.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    
    def upload_file_local(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            self.s3.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download_file_local(self, bucket, object_name, file_name=None):
        try:
            self.s3.download_file(bucket, object_name, object_name if file_name is None else file_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True