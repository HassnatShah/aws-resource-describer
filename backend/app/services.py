# app/services.py

from flask import current_app, jsonify, abort
from app import cache  # Ensure you import the cache instance
import boto3
import logging

logger = logging.getLogger(__name__)

class AWSService:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    @cache.cached(timeout=300)  # Cache for 5 minutes
    def describe_resources(self):
        ec2_client = self.session.client('ec2')
        try:
            instances = ec2_client.describe_instances()
            # Process instances as before
            instance_details = []

            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    details = {
                        'InstanceId': instance.get('InstanceId'),
                        'InstanceType': instance.get('InstanceType'),
                        'State': instance.get('State', {}).get('Name'),
                        'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                        'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                        'SubnetId': instance.get('SubnetId', 'N/A'),
                        'VpcId': instance.get('VpcId', 'N/A'),
                        'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])},
                    }

                    # Get Instance Name from Tags if it exists
                    details['InstanceName'] = details['Tags'].get('Name', 'N/A')
                    
                    instance_details.append(details)

            return instance_details
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing EC2 resources: {e}")
            abort(503, description="Service Unavailable: AWS API error.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            abort(500, description="Internal Server Error")