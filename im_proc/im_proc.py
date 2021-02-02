import paho.mqtt.client as mqtt
import uuid
import sys

#MQTT_HOST = '18.221.177.196'
MQTT_HOST = 'ec2-18-191-197-152.us-east-2.compute.amazonaws.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'faces'

def on_connect_local(client, userdata, flags, rc):
  print("connected to local broker with rc: " + str(rc))

def on_message(client,userdata, msg):
  try:
    print("message received!")
    # sending message to the s3 bucket
    guid = str(uuid.uuid4())
    msg = msg.payload
    file_path = "/mnt/mids-251-hw3-eb/" + "hw03" + guid + ".png"
    with open(file_path, 'wb') as outfile:
      outfile.write(msg)
  except:
    print("Unexpected error:", sys.exc_info()[0])

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect_local
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)

mqttclient.subscribe(MQTT_TOPIC, qos=2)
mqttclient.on_message = on_message

mqttclient.loop_forever()
