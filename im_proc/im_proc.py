import paho.mqtt.client as mqtt
import uuid
import sys

MQTT_HOST = '18.221.177.196'
MQTT_HOST = 'ec2-18-221-177-196.us-east-2.compute.amazonaws.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'hw3'

def on_connect_local(client, userdata, flags, rc):
  print("connected to local broker with rc: " + str(rc))

def on_message(client,userdata, msg):
  try:
    print("message received!")
    print("Received message of len:{} bytes from topic:{}".format(len(msg.payload), msg.topic) )
    # Publishing this message to the cloud broker
    guid = str(uuid.uuid4())
    msg = msg.payload
    file_path = "/mnt/mids-251-hw3-eb/" + "hw03" + guid + ".png"
    with open(file_path, 'wb') as outfile:
      outfile.write(msg)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)
local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()
