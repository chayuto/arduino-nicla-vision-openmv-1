import pyb # Import module for board related functions

redLED = pyb.LED(1) # built-in red LED
greenLED = pyb.LED(2) # built-in green LED
blueLED = pyb.LED(3) # built-in blue LED
delay = 250
while True:

  # Turns on the red LED
  redLED.on()
  # Makes the script wait for 1 second (250 milliseconds)
  pyb.delay(250)
  # Turns off the red LED
  redLED.off()
  pyb.delay(250)
  greenLED.on()
  pyb.delay(250)
  greenLED.off()
  pyb.delay(250)
  blueLED.on()
  pyb.delay(250)
  blueLED.off()
  pyb.delay(250)
