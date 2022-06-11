import paho.mqtt.client as mqtt

#set client variables
LOCAL_MQTT_HOST="nx_broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="hw3"

CLOUD_MQTT_HOST="3.137.201.2"
CLOUD_MQTT_PORT=1883
CLOUD_MQTT_TOPIC="hw3"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))

def on_connect_cloud(client, userdata, flags, rc):
    print("connect to cloud broker with rc: " + str(rc))

def on_message(client,userdata, msg):
  try:
    print("message received!")
    print("Received message: len:{} bytes from topic:{}".format(len(msg.payload), msg.topic) )
    msg = msg.payload
    cloud_mqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg, qos=1, retain=True)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)
local_mqttclient.on_message = on_message

cloud_mqttclient = mqtt.Client()
cloud_mqttclient.on_connect = on_connect_cloud
cloud_mqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)

local_mqttclient.loop_forever()
