# app/routes.py

from flask import Blueprint, jsonify, request, abort
from app.services.service_registry import ServiceRegistry

api_bp = Blueprint('api', __name__)

@api_bp.route('/services', methods=['GET'])
def list_services():
    services = ServiceRegistry.get_all_services()
    return jsonify({'services': services})

@api_bp.route('/services/<service_name>', methods=['GET'])
def list_subservices(service_name):
    try:
        service = ServiceRegistry.get_service(service_name)
        subservices = service.get_subservices()
        return jsonify({'subservices': subservices})
    except ValueError as e:
        abort(404, description=str(e))

@api_bp.route('/services/<service_name>/<subservice_name>', methods=['GET'])
def describe_subservice(service_name, subservice_name):
    try:
        service = ServiceRegistry.get_service(service_name)
        data = service.describe_subservice(subservice_name, **request.args)
        return jsonify({'data': data})
    except ValueError as e:
        abort(404, description=str(e))