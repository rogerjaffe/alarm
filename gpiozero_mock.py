from pynput import keyboard
import re

zone_state_idx = ["4","17","27","22","18","23","5"]
zone_state = {
  "4": {
    "state": False,
    "ref": None
  },
  "17": {
    "state": False,
    "ref": None
  },
  "27": {
    "state": False,
    "ref": None
  },
  "22": {
    "state": False,
    "ref": None
  },
  "18": {
    "state": False,
    "ref": None
  },
  "23": {
    "state": False,
    "ref": None
  },
  "5": {
    "state": False,
    "ref": None
  },
}

class Pin:
  def __init__(self, _number):
    self.number = _number

class LED:

  def __init__(self, _number):
    pass

  def on(self):
    pass
    # print("LED_ON")

  def off(self):
    pass
    # print("LED_OFF")

class Button:

  def __init__(self, pin, pull_up=None):
    self.pin = Pin(pin)
    self.pull_up = pull_up
    zone_state[pin]["ref"] = self

  def when_pressed(self, btn):
    pass

  def when_released(self, btn):
    pass

def valid_zone(char):
  return re.search('[0-6]', char)

def on_key(char):
  if (valid_zone(char)):
    key = zone_state_idx[int(char)]
    zone = zone_state[key]
    zone["state"] = not zone["state"]
    if (zone["state"]):
      zone["ref"].when_pressed(zone["ref"])
    else:
      zone["ref"].when_released(zone["ref"])

def on_press(key):
  try:
    on_key(key.char)
  except AttributeError:
    print('special key {0} pressed'.format(
      key))

listener = keyboard.Listener(
  on_press=on_press)
listener.start()
