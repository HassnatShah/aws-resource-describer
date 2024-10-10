import boto3
from flask import current_app

class AWSService:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    def describe_resources(self):
        ec2_client = self.session.client('ec2')
        instances = ec2_client.describe_instances()
        # Process instances data as needed
        return instances
    
    def describe_s3_buckets(self):
        s3_client = self.session.client('s3')
        buckets = s3_client.list_buckets()
        return buckets