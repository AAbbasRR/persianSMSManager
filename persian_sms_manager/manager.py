from typing import Type, Dict, Any
from .raygansms import RayganSMSService

class SMSManager:
    """
    Manages different SMS services and provides a unified interface for creating service instances.

    Attributes:
        services (Dict[str, Type[RayganSMSService]]): A dictionary mapping service names to service classes.
    """
    
    services: Dict[str, Type[RayganSMSService]] = {
        "raygansms": RayganSMSService
    }

    def __new__(cls, service_name: str, user_mobile: str, **kwargs: Any) -> RayganSMSService:
        """
        Retrieves an instance of the specified SMS service based on the service name.

        Args:
            service_name (str): The name of the SMS service to retrieve.
            user_mobile (str): The mobile number of the user.
            **kwargs (Any): Additional keyword arguments passed to the SMS service constructor.

        Returns:
            RayganSMSService: An instance of the specified SMS service.

        Raises:
            ValueError: If the provided service name is invalid.
        """
        service_class = cls.services.get(service_name.lower())
        if not service_class:
            raise ValueError(f"Invalid service name: {service_name}. Available services: {list(SMSManager.services.keys())}")

        return service_class(user_mobile, **kwargs)


