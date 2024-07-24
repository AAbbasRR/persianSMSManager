from abc import ABC, abstractmethod

class BaseSMSService(ABC):
    """
    An abstract base class for SMS services.

    Attributes:
        user_mobile (str): The mobile number of the user.
    """

    def __init__(self, user_mobile: str, **kwargs: any) -> None:
        """
        Initializes the BaseSMSService with the user's mobile number.

        Args:
            user_mobile (str): The mobile number of the user.
            **kwargs (Any): Additional keyword arguments (not used in this base class).
        """
        self.user_mobile: str = user_mobile

    @abstractmethod
    def send_message(self, message: str) -> bool:
        """
        Send a message to the user's mobile number.

        Args:
            message (str): The message content to send.

        Returns:
            bool: True if the message was successfully sent, otherwise False.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def send_otp_code(self, title_type: str) -> bool:
        """
        Send an OTP code with a specific title type to the user's mobile number.

        Args:
            title_type (str): The type or title of the OTP message.

        Returns:
            bool: True if the OTP code was successfully sent, otherwise False.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def check_otp_code_existed(self) -> bool:
        """
        Check if an OTP code exists for the user's mobile number.

        Returns:
            bool: True if the OTP code exists, otherwise False.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def send_auto_otp_code(self) -> bool:
        """
        Send an auto-generated OTP code to the user's mobile number.

        Returns:
            bool: True if the OTP code was successfully sent, otherwise False.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def check_auto_otp_code(self, otp_code: str) -> bool:
        """
        Verify the auto-generated OTP code sent to the user's mobile number.

        Args:
            otp_code (str): The OTP code to verify.

        Returns:
            bool: True if the OTP code is valid, otherwise False.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

