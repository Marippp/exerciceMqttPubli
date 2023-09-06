
import RPi.GPIO as GPIO
import dht11
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

instance = dht11.DHT11(pin=17)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()

client.on_connect = on_connect

client.connect("10.4.1.42", 1883, 60)
while True:
    result = instance.read()
    if result.is_valid():
        client.publish("Marina/Temperature", payload=result.temperature, qos=1, retain=True)
        print("Temperature: %-3.1f C" % result.temperature)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(2)

# print("Humidity: %-3.1f %%" % result.humidity)