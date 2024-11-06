# app/services/s3_service.py

import boto3
from flask import current_app, abort
import logging
from app import cache
from app.services.base_service import BaseService

logger = logging.getLogger(__name__)

class S3Service(BaseService):
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    def get_subservices(self):
        return ['buckets']

    @cache.cached(timeout=300, key_prefix='s3_buckets')
    def describe_subservice(self, subservice_name, **kwargs):
        if subservice_name == 'buckets':
            return self.describe_buckets()
        else:
            abort(404, description="Subservice not found.")

    def describe_buckets(self):
        s3_client = self.session.client('s3')
        try:
            response = s3_client.list_buckets()
            buckets = []
            for bucket in response.get('Buckets', []):
                details = {
                    'Name': bucket.get('Name', 'N/A'),
                    'CreationDate': bucket.get('CreationDate').isoformat() if bucket.get('CreationDate') else 'N/A',
                }
                # Optionally, fetch more details like tags
                try:
                    tagging = s3_client.get_bucket_tagging(Bucket=bucket['Name'])
                    tags = {tag['Key']: tag['Value'] for tag in tagging.get('TagSet', [])}
                    details['Tags'] = tags
                except s3_client.exceptions.NoSuchTagSet:
                    details['Tags'] = {}
                buckets.append(details)
            return buckets
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing S3 buckets: {e}")
            abort(503, description="Service Unavailable: AWS API error.")