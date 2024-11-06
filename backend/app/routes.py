# app/routes.py

from flask import Blueprint, jsonify, make_response
from app.services import AWSService

api_bp = Blueprint('api', __name__)

@api_bp.route('/describe-resources', methods=['GET'])
def describe_resources():
    aws_service = AWSService()
    resources = aws_service.describe_resources()
    return jsonify({'Instances': resources})

# Error handlers
@api_bp.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': str(error)}), 400)

@api_bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@api_bp.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@api_bp.errorhandler(503)
def service_unavailable(error):
    return make_response(jsonify({'error': str(error)}), 503)