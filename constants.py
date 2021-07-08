# !/usr/local/bin/python
# -*- coding: utf-8 -*-

LOST_CONNECTION_THRESHOLD = 90 * 1000   # 90 seconds
SMS_CARRIER = "twilio"
DATABASE_URL = "https://alarm-ab87e.firebaseio.com/"

TIME_BETWEEN_PINGS = 60 * 1000; # 60 seconds

PILOT_LIGHT_PIN = 24
TIME_ON = 0.05
TIME_OFF = 2.95

LOGGER_PATH = 'logs/'
LOGGER_EXT = '.log'
LOGGER_DATE_CHECK_INTERVAL = 5

TWILIO_FROM = "+18582585959"
TWILIO_TO = [
  # "+16192089881",
  "+16192089882",
  # "+18588764375"
]

EMAIL_TO = [
  {
    "Email": "rogerjaffe@gmail.com",
    "Name": "Roger Jaffe"
  },
  # {
  #   "Email": "cathyjaffe@gmail.com",
  #   "Name": "Cathy Jaffe"
  # }
]

GPIOS = {
  "4": {
    "ZONE_ID": 0,
    "PIN": 7,
    "DESCRIPTION": "Front door / living room",
    "GPIO": 4,
    "PULL": False,
  },
  "5": {
    "ZONE_ID": 6,
    "PIN": 29,
    "DESCRIPTION": "Garage door",
    "GPIO": 5,
    "PULL": False
  },
  "17": {
    "ZONE_ID": 1,
    "PIN": 11,
    "DESCRIPTION": "Front bedrooms / Garage door",
    "GPIO": 17,
    "PULL": False
  },
  "27":{
    "ZONE_ID": 2,
    "PIN": 13,
    "DESCRIPTION": "North side windows",
    "GPIO": 27,
    "PULL": False
  },
  "22": {
    "ZONE_ID": 3,
    "PIN": 15,
    "DESCRIPTION": "Master bedroom",
    "GPIO": 22,
    "PULL": False
  },
  "18": {
    "ZONE_ID": 4,
    "PIN": 12,
    "DESCRIPTION": "South bedrooms / bathroom",
    "GPIO": 18,
    "PULL": False
  },
  "23": {
    "ZONE_ID": 5,
    "PIN": 16,
    "DESCRIPTION": "Backyard sliding door",
    "GPIO": 23,
    "PULL": False
  },
}
