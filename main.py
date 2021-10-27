from photo import photo
import time

import RPi.GPIO as GPIO

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

state = 1

GPIO.output(pin,state)

p = photo(0x48)

while True:
  print("{}" .format(p.readPhoto()))
  time.sleep(.1)
  