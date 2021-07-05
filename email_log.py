from datetime import date
from threading import Timer
import constants
import base64

class Email_Log:

  def __init__(self):
    self.today = "2021-07-03"
    Timer(constants.LOGGER_DATE_CHECK_INTERVAL, self.check_date).start()

  def check_date(self):
    today = date.today().strftime("%Y-%m-%d")
    if (self.today != today and self.today != ""):
      self.send_file(self.today)
      self.today = today
    Timer(constants.LOGGER_DATE_CHECK_INTERVAL, self.check_date).start()

  def open_file_to_base64(self, file_name):
    log_data = open(file_name, "r").read()
    log_data_bytes = log_data.encode('ascii')
    base64_bytes = base64.b64encode(log_data_bytes)
    base64_ascii = ""
    for a_byte in base64_bytes:
      base64_ascii += chr(a_byte)
    return base64_ascii

  def send_file(self, dated_filename):
    from mailjet_rest import Client
    import os
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    file_name = constants.LOGGER_PATH+dated_filename+constants.LOGGER_EXT
    base64_ascii = self.open_file_to_base64(file_name)
    data = {
      'Messages': [
        {
          "From": {
            "Email": "rogerjaffe@gmail.com",
            "Name": "Roger Jaffe"
          },
          "To": constants.EMAIL_TO,
          "Subject": "Alarm sensor log for "+dated_filename,
          "TextPart": "See attached file",
          "HTMLPart": "<h3>See attached file</h3>",
          "Attachments": [
            {
              "ContentType": "text/plain",
              "Filename": file_name,
              "Base64Content": base64_ascii
            }
          ]
        }
      ]
    }
    result = mailjet.send.create(data=data)
    print('Alarm sensor log for '+dated_filename+' sent')
