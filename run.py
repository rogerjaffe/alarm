#################################################################
# Alarm notification system
# Texts when sensor is tripped or reset
# Email log file each day
#################################################################
# Import gpiozero if a R-Pi, otherwise input the mocked version
# platform.node() == "alarmpi" if device is a R-Pi
import platform
node = platform.node()
if (node == "alarmpi"):
    from gpiozero import *
else:
    from gpiozero_mock import *

#################################################################
# Pilot light configuration
# Flashes the LED connected to pin 24 every 3 seconds
import constants
from threading import Timer
# Create the LED object
led = LED(constants.PILOT_LIGHT_PIN)
def pilot_off():
    Timer(constants.TIME_OFF, pilot_on).start()
    led.off()

def pilot_on():
    Timer(constants.TIME_ON, pilot_off).start()
    led.on()

pilot_on()

#################################################################
# Configure text messaging
from text_messaging import Text_Messaging
text = Text_Messaging()
text.sendText("Alarm monitoring is starting")

#################################################################
# Print status message
print("Alarm sensor monitoring starting up")


#################################################################
# Zone tripped / reset functions
def zone_tripped(btn):
    import alarm_logger
    message = constants.GPIOS[str(btn.pin.number)]["DESCRIPTION"]+" TRIPPED"
    alarm_logger.log_message(message)
    text.sendText(message)
    print(message)

def zone_reset(btn):
    import alarm_logger
    message = constants.GPIOS[str(btn.pin.number)]["DESCRIPTION"] + " RESET"
    alarm_logger.log_message(message)
    text.sendText(message)
    print(message)

#################################################################
# Set up logger daily email
from email_log import Email_Log
email_log = Email_Log()

#################################################################
# Set up alarm sensors as buttons
buttons = []
for gpio in constants.GPIOS:
    button = Button(gpio, pull_up=False)
    button.when_pressed = zone_tripped
    button.when_released = zone_reset
    buttons.append(button)
    print(constants.GPIOS[gpio]["DESCRIPTION"]+" configured")

# Wait for stuff to happen!
from signal import pause
pause()
