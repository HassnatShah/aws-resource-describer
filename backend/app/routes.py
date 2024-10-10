from flask import Blueprint, jsonify
from app.services import AWSService

api_bp = Blueprint('api', __name__)

@api_bp.route('/describe-resources', methods=['GET'])
def describe_resources():
    aws_service = AWSService()
    resources = aws_service.describe_resources()
    return jsonify(resources)