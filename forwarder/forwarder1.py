import paho.mqtt.client as mqtt
import time

remote_client = mqtt.Client()

remote_client.connect("3.137.201.2",1883,60)

def post_face_remote(face):
    try:
        remote_client.publish("hw3", payload=msg, qos=0, retain=False);
    except:
        print("Unexpected error:", sys.exc_info()[0])
    #remote_client.disconnect();

def on_connect_local(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("hw3",qos=1)

def on_message(client, userdata, msg):
    print("on message received")
    post_face_remote(msg.payload)

client = mqtt.Client(transport="tcp")

client.connect("nx_broker",1883,60)
client.on_connect = on_connect_local
client.on_message = on_message

client.loop_forever()
