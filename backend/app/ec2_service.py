# app/services/ec2_service.py

import boto3
from flask import current_app, abort
import logging
from app import cache
from app.services.base_service import BaseService

logger = logging.getLogger(__name__)

class EC2Service(BaseService):
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    def get_subservices(self):
        return ['instances', 'security-groups']

    @cache.cached(timeout=300, key_prefix='ec2_instances')
    def describe_subservice(self, subservice_name, **kwargs):
        if subservice_name == 'instances':
            return self.describe_instances()
        elif subservice_name == 'security-groups':
            return self.describe_security_groups()
        else:
            abort(404, description="Subservice not found.")

    def describe_instances(self):
        ec2_client = self.session.client('ec2')
        try:
            instances = ec2_client.describe_instances()
            instance_details = []
            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    details = {
                        'InstanceId': instance.get('InstanceId', 'N/A'),
                        'InstanceType': instance.get('InstanceType', 'N/A'),
                        'State': instance.get('State', {}).get('Name', 'N/A'),
                        'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                        'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                        'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])},
                        # Add more fields as needed
                    }
                    instance_details.append(details)
            return instance_details
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing EC2 instances: {e}")
            abort(503, description="Service Unavailable: AWS API error.")

    def describe_security_groups(self):
        ec2_client = self.session.client('ec2')
        try:
            security_groups = ec2_client.describe_security_groups()
            sg_details = []
            for sg in security_groups['SecurityGroups']:
                details = {
                    'GroupId': sg.get('GroupId', 'N/A'),
                    'GroupName': sg.get('GroupName', 'N/A'),
                    'Description': sg.get('Description', 'N/A'),
                    'VpcId': sg.get('VpcId', 'N/A'),
                    'Tags': {tag['Key']: tag['Value'] for tag in sg.get('Tags', [])},
                    # Add more fields as needed
                }
                sg_details.append(details)
            return sg_details
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing Security Groups: {e}")
            abort(503, description="Service Unavailable: AWS API error.")