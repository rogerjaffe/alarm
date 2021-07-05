# Download the Python helper library from twilio.com/docs/python/install
import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client
import constants

class Text_Messaging:
  def __init__(self):
    # Your Account Sid and Auth Token from the Python environment
    self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
    self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # self.messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']

  def sendText(self, message):
    for text_to in constants.TWILIO_TO:
      client = Client(self.account_sid, self.auth_token)
      message = client.messages.create(
        body=message,
        from_=constants.TWILIO_FROM,
        to=text_to
      )
      print(message.sid)



