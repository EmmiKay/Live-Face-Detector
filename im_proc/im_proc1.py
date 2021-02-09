import paho.mqtt.client as mqtt
import time
import uuid


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("hw3", qos=1)

def on_message(client, userdata, msg):
    guid = str(uuid.uuid4())
    try:
        f = open("/mnt/mids-251-hw3-eb/" + "hw03" + guid + ".png")
        f.write(msg.payload)
        f.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])

client = mqtt.Client()
client.connect("3.137.201.2",1883,20)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
