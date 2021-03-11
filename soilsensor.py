import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 2

GPIO.setup(PIN, GPIO.IN)

while True:
    print(GPIO.input(PIN))
    time.sleep(1000)
