# app/services/waf_service.py

import boto3
from flask import current_app, abort
import logging
from app import cache
from app.services.base_service import BaseService

logger = logging.getLogger(__name__)

class WAFService(BaseService):
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
            region_name=current_app.config['AWS_DEFAULT_REGION']
        )

    def get_subservices(self):
        return ['global', 'regional']

    @cache.cached(timeout=300, key_prefix='waf_global')
    def describe_subservice(self, subservice_name, **kwargs):
        if subservice_name == 'global':
            return self.describe_global_waf()
        elif subservice_name == 'regional':
            return self.describe_regional_waf()
        else:
            abort(404, description="Subservice not found.")

    def describe_global_waf(self):
        waf_client = self.session.client('wafv2', region_name='us-east-1')  # Global WAF is in us-east-1
        try:
            # Example: List Web ACLs
            response = waf_client.list_web_acls(Scope='CLOUDFRONT')
            web_acls = response.get('WebACLs', [])
            return web_acls
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing Global WAF: {e}")
            abort(503, description="Service Unavailable: AWS API error.")

    def describe_regional_waf(self):
        waf_client = self.session.client('wafv2', region_name=current_app.config['AWS_DEFAULT_REGION'])
        try:
            # Example: List Web ACLs
            response = waf_client.list_web_acls(Scope='REGIONAL')
            web_acls = response.get('WebACLs', [])
            return web_acls
        except boto3.exceptions.Boto3Error as e:
            logger.error(f"Error describing Regional WAF: {e}")
            abort(503, description="Service Unavailable: AWS API error.")