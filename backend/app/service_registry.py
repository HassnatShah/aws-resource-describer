# app/services/service_registry.py

from app.services.ec2_service import EC2Service
from app.services.waf_service import WAFService
from app.services.s3_service import S3Service

class ServiceRegistry:
    _services = {}

    @classmethod
    def register_service(cls, service_name, service_class):
        cls._services[service_name.lower()] = service_class()

    @classmethod
    def get_service(cls, service_name):
        service = cls._services.get(service_name.lower())
        if not service:
            raise ValueError(f"Service '{service_name}' not found.")
        return service

    @classmethod
    def get_all_services(cls):
        return list(cls._services.keys())

# Register services
ServiceRegistry.register_service('ec2', EC2Service)
ServiceRegistry.register_service('waf', WAFService)
ServiceRegistry.register_service('s3', S3Service)  # Newly added