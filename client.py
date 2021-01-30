import paho.mqtt.client as mqtt #import the client1
import os


MQTT_BROKER = os.getenv('MQTT)')

client = mqtt.Client("P1") #create new instance
client.connect(MQTT_BROKER) #connect to broker
client.publish("example","Hello World")#publish

print("send done")
