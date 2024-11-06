# app/services/base_service.py

from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def get_subservices(self):
        """Return a list of available sub-services."""
        pass

    @abstractmethod
    def describe_subservice(self, subservice_name, **kwargs):
        """Describe a specific sub-service."""
        pass