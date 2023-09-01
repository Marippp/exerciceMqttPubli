
import RPi.GPIO as GPIO
import dht11
import paho.mqtt.publish as publish
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=17)


#publish.single("paho/test/single", "payload", hostname="test.mosquitto.org")
while(True):
    result = instance.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(1)