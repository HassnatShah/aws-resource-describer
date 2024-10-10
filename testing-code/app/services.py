# # import boto3
# # from flask import current_app

# # class AWSService:
# #     def __init__(self):
# #         self.session = boto3.Session(
# #             aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
# #             aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
# #             region_name=current_app.config['AWS_DEFAULT_REGION']
# #         )

# #     def describe_resources(self):
# #         ec2_client = self.session.client('ec2')
# #         instances = ec2_client.describe_instances()
# #         # Process instances data as needed
# #         return instances
    
# #     def describe_s3_buckets(self):
# #         s3_client = self.session.client('s3')
# #         buckets = s3_client.list_buckets()
# #         return buckets

# import boto3
# from flask import current_app

# class AWSService:
#     def __init__(self):
#         self.session = boto3.Session(
#             aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
#             aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
#             region_name=current_app.config['AWS_DEFAULT_REGION']
#         )

#     def describe_resources(self):
#         ec2_client = self.session.client('ec2')
#         instances = ec2_client.describe_instances()
        
#         instance_details = []

#         for reservation in instances['Reservations']:
#             for instance in reservation['Instances']:
#                 details = {
#                     'InstanceId': instance.get('InstanceId'),
#                     'InstanceType': instance.get('InstanceType'),
#                     'State': instance.get('State', {}).get('Name'),
#                     'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
#                     'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
#                     'SubnetId': instance.get('SubnetId', 'N/A'),
#                     'VpcId': instance.get('VpcId', 'N/A'),
#                     'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])},
#                 }

#                 # Get Instance Name from Tags if it exists
#                 details['InstanceName'] = details['Tags'].get('Name', 'N/A')
                
#                 instance_details.append(details)

#         return instance_details

import boto3
from flask import current_app, jsonify
import logging

logger = logging.getLogger(__name__)

class AWSService:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    def describe_resources(self):
        ec2_client = self.session.client('ec2')
        try:
            instances = ec2_client.describe_instances()
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
        except Exception as e:
            logger.error(f"Error describing EC2 resources: {e}")
            return jsonify({"error": "Could not describe resources"}), 500
