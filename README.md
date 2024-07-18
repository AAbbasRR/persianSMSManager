# Iranian SMS Manager

A Python package for managing Iranian SMS services, providing support for multiple SMS providers and a modular,
extensible design.

## Requirements

- Python 3.11+
- requests

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/AAbbasRR/persianSMSManager.git
```

Alternatively, clone the repository and install manually:

```bash
git clone https://github.com/AAbbasRR/persianSMSManager.git
cd persianSMSManager
pip install .
```

or

```sh
pip install persian_sms_manager
```

## Usage

This package allows you to send SMS messages, including OTP (One-Time Password) codes, through various SMS services.
Currently, it supports RayganSMS and AnotherSMSService.

## Configuration

You need to configure the SMS service you want to use. Here is an example for RayganSMS and AnotherSMSService.

Example with RayganSMS:

```python
from persian_sms_manager import SMSManager

# Configure RayganSMS
sms_manager = SMSManager(
    service_name="raygansms",
    user_mobile="09123456789",
    username="your_username",
    password="your_password"
)

# Send a message
sms_manager.service.send_message("This is a test message")

# Send OTP code
sms_manager.service.send_otp_code("register")

# Send automatic OTP code
sms_manager.service.send_auto_otp_code()

# Check automatic OTP code
valid = sms_manager.service.check_auto_otp_code("123456")
```

## Adding New SMS Services

To add support for a new SMS service, create a new class in the package that inherits from BaseSMSService and implements
the required methods. Then, update the SMSManager class to include this new service.

### Example

Create a file new_sms_service.py:

```python
from persian_sms_manager.base import BaseSMSService
import requests


class NewSMSService(BaseSMSService):
    def __init__(self, user_mobile, api_key):
        super().__init__(user_mobile)
        self.api_key = api_key

    def send_request(self, endpoint, data):
        data.update({
            "api_key": self.api_key,
        })
        response = requests.post(f"https://new-sms-service.com/{endpoint}", data=data)
        return response.status_code == 200

    def send_message(self, message):
        data = {
            "mobile": self.user_mobile,
            "message": message,
        }
        return self.send_request("send_message", data)

    def send_otp_code(self, title_type):
        otp_code = "12345"
        message = f"your otp: {otp_code}."
        return self.send_message(message)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

Abbas Rahimzadeh - [arahimzadeh79@gmail.com](mailto:arahimzadeh79@gmail.com)

## Acknowledgments

Special thanks to the open-source community for their valuable contributions and resources.