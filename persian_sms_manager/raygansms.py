import requests
from .base import BaseSMSService


class RayganSMSService(BaseSMSService):
    api_url = "https://raygansms.com/"

    def __init__(self, user_mobile, username, password):
        super().__init__(user_mobile)
        self.username = username
        self.password = password

    def send_request(self, endpoint, data):
        data.update({
            "UserName": self.username,
            "Password": self.password,
        })
        response = requests.post(f"{self.api_url}{endpoint}", data=data)
        return response.status_code == 200

    def send_message(self, message):
        data = {
            "Mobile": self.user_mobile,
            "Message": message,
        }
        return self.send_request("SendMessageWithCode.ashx", data)

    def send_auto_otp_code(self, footer=""):
        data = {
            "Mobile": self.user_mobile,
            "Footer": footer,
        }
        return self.send_request("AutoSendCode.ashx", data)

    def check_auto_otp_code(self, otp_code):
        data = {
            "Mobile": self.user_mobile,
            "Code": str(otp_code),
        }
        return self.send_request("CheckSendCode.ashx", data)
