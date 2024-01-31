from twilio.rest import Client

account_sid = "ACb0496837f5e7c00904db1ff027672de1"
auth_token = "a8d9b96bcabce7d38a0082881a79d474"


class NotificationManager:

    def __init__(self):
        self.content = ""
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self):
        """Send message via Twilio"""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=self.content,
            from_="+14696063576",
            to="+40727855511"
        )
        print(f"The status of the Twilio sms is: {message.status}")
