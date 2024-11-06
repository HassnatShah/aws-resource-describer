import boto3
from flask import current_app, abort
import logging
from app import cache  # Ensure this import is correct

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
            instance_details = []

            for reservation in instances['Reservations']:
                for instance in reservation['Instances']:
                    details = {
                        'InstanceId': instance.get('InstanceId', 'N/A'),
                        'InstanceType': instance.get('InstanceType', 'N/A'),
                        'State': {
                            'Code': instance.get('State', {}).get('Code', 'N/A'),
                            'Name': instance.get('State', {}).get('Name', 'N/A')
                        },
                        'PublicDnsName': instance.get('PublicDnsName', 'N/A'),
                        'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                        'PrivateDnsName': instance.get('PrivateDnsName', 'N/A'),
                        'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                        'KeyName': instance.get('KeyName', 'N/A'),
                        'SecurityGroups': [
                            {
                                'GroupName': sg.get('GroupName', 'N/A'),
                                'GroupId': sg.get('GroupId', 'N/A')
                            } for sg in instance.get('SecurityGroups', [])
                        ],
                        'LaunchTime': instance.get('LaunchTime').isoformat() if instance.get('LaunchTime') else 'N/A',
                        'Placement': {
                            'AvailabilityZone': instance.get('Placement', {}).get('AvailabilityZone', 'N/A'),
                            'Tenancy': instance.get('Placement', {}).get('Tenancy', 'N/A'),
                            'GroupName': instance.get('Placement', {}).get('GroupName', 'N/A')
                        },
                        'ImageId': instance.get('ImageId', 'N/A'),
                        'BlockDeviceMappings': [
                            {
                                'DeviceName': bdm.get('DeviceName', 'N/A'),
                                'Ebs': {
                                    'VolumeId': bdm.get('Ebs', {}).get('VolumeId', 'N/A'),
                                    'DeleteOnTermination': bdm.get('Ebs', {}).get('DeleteOnTermination', 'N/A')
                                }
                            } for bdm in instance.get('BlockDeviceMappings', [])
                        ],
                        'IamInstanceProfile': {
                            'Arn': instance.get('IamInstanceProfile', {}).get('Arn', 'N/A'),
                            'Id': instance.get('IamInstanceProfile', {}).get('Id', 'N/A')
                        },
                        'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])},
                        'NetworkInterfaces': [
                            {
                                'NetworkInterfaceId': ni.get('NetworkInterfaceId', 'N/A'),
                                'PrivateIpAddress': ni.get('PrivateIpAddress', 'N/A'),
                                'MacAddress': ni.get('MacAddress', 'N/A'),
                                'SubnetId': ni.get('SubnetId', 'N/A')
                            } for ni in instance.get('NetworkInterfaces', [])
                        ],
                        'Hypervisor': instance.get('Hypervisor', 'N/A'),
                        'Platform': instance.get('Platform', 'N/A'),
                        'Monitoring': instance.get('Monitoring', {}).get('State', 'N/A'),
                        'SourceDestCheck': instance.get('SourceDestCheck', 'N/A'),
                        'SpotInstanceRequestId': instance.get('SpotInstanceRequestId', 'N/A'),
                        'EbsOptimized': instance.get('EbsOptimized', 'N/A'),
                        'CpuOptions': {
                            'CoreCount': instance.get('CpuOptions', {}).get('CoreCount', 'N/A'),
                            'ThreadsPerCore': instance.get('CpuOptions', {}).get('ThreadsPerCore', 'N/A')
                        },
                        'ElasticGpuAssociations': instance.get('ElasticGpuAssociations', []),
                        'MetadataOptions': {
                            'HttpTokens': instance.get('MetadataOptions', {}).get('HttpTokens', 'N/A'),
                            'HttpEndpoint': instance.get('MetadataOptions', {}).get('HttpEndpoint', 'N/A')
                        },
                        'LaunchTemplate': instance.get('LaunchTemplate', {}).get('LaunchTemplateId', 'N/A')
                    }
                    instance_details.append(details)

            return instance_details
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing EC2 resources: {e}")
            abort(503, description="Service Unavailable: AWS API error.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            abort(500, description="Internal Server Error")