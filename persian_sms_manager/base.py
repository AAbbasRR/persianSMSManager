class BaseSMSService:
    def __init__(self, user_mobile, **kwargs):
        self.user_mobile = user_mobile

    def send_message(self, message):
        raise NotImplementedError("This method should be overridden by subclasses")

    def send_otp_code(self, title_type):
        raise NotImplementedError("This method should be overridden by subclasses")

    def check_otp_code_existed(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def send_auto_otp_code(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def check_auto_otp_code(self, otp_code):
        raise NotImplementedError("This method should be overridden by subclasses")
