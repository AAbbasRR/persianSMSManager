import requests
from typing import Optional, Union

from .base import BaseSMSService

class RayganSMSService(BaseSMSService):
    """
    A service for sending SMS messages using the Raygan SMS API.

    Attributes:
        api_url (str): Base URL for the Raygan SMS API.
        username (str): API username for authentication.
        password (str): API password for authentication.
    """
    
    api_url: str = "https://raygansms.com/"

    def __init__(self, user_mobile: str, username: str, password: str) -> None:
        """
        Initialize the RayganSMSService with user mobile number, username, and password.

        Args:
            user_mobile (str): The mobile number of the user.
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        super().__init__(user_mobile)
        self.username: str = username
        self.password: str = password

    def send_request(self, endpoint: str, data: dict[str, str]) -> bool:
        """
        Send a request to the specified API endpoint with the given data.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict[str, str]): The data to send in the request.

        Returns:
            bool: True if the request was successful (HTTP status code 200), otherwise False.
        """
        data.update({
            "UserName": self.username,
            "Password": self.password,
        })
        try:
            response = requests.post(f"{self.api_url}{endpoint}", data=data)
            response.raise_for_status()
            return response.status_code == 200
        except requests.RequestException as e:
            # Optionally log the exception or handle it as needed
            print(f"An error occurred: {e}")
            return False

    def send_message(self, message: str) -> bool:
        """
        Send a message to the user's mobile number.

        Args:
            message (str): The message content to send.

        Returns:
            bool: True if the message was successfully sent, otherwise False.
        """
        data = {
            "Mobile": self.user_mobile,
            "Message": message,
        }
        return self.send_request("SendMessageWithCode.ashx", data)

    def send_auto_otp_code(self, footer: Optional[str] = "") -> bool:
        """
        Send an auto-generated OTP code to the user's mobile number.

        Args:
            footer (Optional[str]): Optional footer to include in the OTP message.

        Returns:
            bool: True if the OTP code was successfully sent, otherwise False.
        """
        data = {
            "Mobile": self.user_mobile,
            "Footer": footer,
        }
        return self.send_request("AutoSendCode.ashx", data)

    def check_auto_otp_code(self, otp_code: Union[str, int]) -> bool:
        """
        Verify the OTP code sent to the user's mobile number.

        Args:
            otp_code (Union[str, int]): The OTP code to verify.

        Returns:
            bool: True if the OTP code is valid, otherwise False.
        """
        data = {
            "Mobile": self.user_mobile,
            "Code": str(otp_code),
        }
        return self.send_request("CheckSendCode.ashx", data)

