import time
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 22 

GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
print("Short BCM %s to HIGH 3.3V to trigger action...", button)
print("@see pinout command or https://pinout.xyz for layout")
while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
      print ("connected")
    time.sleep(0.5)


GPIO.cleanup()
