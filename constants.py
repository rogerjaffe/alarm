# !/usr/local/bin/python
# -*- coding: utf-8 -*-

LOST_CONNECTION_THRESHOLD = 90 * 1000   # 90 seconds
SMS_CARRIER = "twilio"
DATABASE_URL = "https://alarm-ab87e.firebaseio.com/"

TIME_BETWEEN_PINGS = 60 * 1000; # 60 seconds

PILOT_LIGHT_PIN = 19
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
    "DESCRIPTION": "Zone 0: Family, Emily, Adam",
    "GPIO": 4,
    "PULL": False,
  },
  "5": {
    "ZONE_ID": 1,
    "PIN": 29,
    "DESCRIPTION": "Zone 1: Sam bath window",
    "GPIO": 5,
    "PULL": False
  },
  "17": {
    "ZONE_ID": 2,
    "PIN": 11,
    "DESCRIPTION": "Zone 2: Back door",
    "GPIO": 17,
    "PULL": False
  },
  "27":{
    "ZONE_ID": 3,
    "PIN": 13,
    "DESCRIPTION": "Zone 3: Garage window",
    "GPIO": 27,
    "PULL": False
  },
  "22": {
    "ZONE_ID": 4,
    "PIN": 15,
    "DESCRIPTION": "Zone 4: Living room window",
    "GPIO": 22,
    "PULL": False
  },
  "18": {
    "ZONE_ID": 5,
    "PIN": 12,
    "DESCRIPTION": "Zone 5: Guest bedroom window",
    "GPIO": 18,
    "PULL": False
  },
  "23": {
    "ZONE_ID": 6,
    "PIN": 16,
    "DESCRIPTION": "Zone 6: Ben left window",
    "GPIO": 23,
    "PULL": False
  },
  "6": {
    "ZONE_ID": 7,
    "PIN": 31,
    "DESCRIPTION": "Zone 7: Front door",
    "GPIO": 6,
    "PULL": False
  },
  "26": {
    "ZONE_ID": 8,
    "PIN": 37,
    "DESCRIPTION": "Zone 8: Sam window",
    "GPIO": 26,
    "PULL": False
  },
  "24": {
    "ZONE_ID": 9,
    "PIN": 18,
    "DESCRIPTION": "Zone 9: Master bedroom left window",
    "GPIO": 24,
    "PULL": False
  },
  "25": {
    "ZONE_ID": 10,
    "PIN": 22,
    "DESCRIPTION": "Zone 10: Master bedroom right window",
    "GPIO": 25,
    "PULL": False
  },
  "16": {
    "ZONE_ID": 11,
    "PIN": 36,
    "DESCRIPTION": "Zone 11: Ben right window",
    "GPIO": 16,
    "PULL": False
  },
  "13": {
    "ZONE_ID": 12,
    "PIN": 33,
    "DESCRIPTION": "Zone 12: Garage side door",
    "GPIO": 13,
    "PULL": False
  }
}
