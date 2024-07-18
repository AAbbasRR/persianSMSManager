from .raygansms import RayganSMSService


class SMSManager:
    def __init__(self, service_name, user_mobile, **kwargs):
        self.services = {
            "raygansms": RayganSMSService
        }
        self.service = self.get_service(service_name, user_mobile, **kwargs)

    def get_service(self, service_name, user_mobile, **kwargs):
        service_class = self.services.get(service_name.lower())
        if not service_class:
            raise ValueError(f"Invalid service name: {service_name}, available services: {list(self.services.keys())}")

        return service_class(user_mobile, **kwargs)
