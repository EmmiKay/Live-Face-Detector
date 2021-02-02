import paho.mqtt.client as mqtt

MQTT_HOST = 'nx_broker'
#MQTT_HOST = '73.101.143.198'
MQTT_PORT = 1883
MQTT_TOPIC = "hw3"

#CLOUD_MQTT_HOST = '18.221.177.196'
CLOUD_MQTT_HOST = 'ec2-18-191-197-152.us-east-2.compute.amazonaws.com'
CLOUD_MQTT_PORT = 1883
CLOUD_MQTT_TOPIC = 'face_detect'

def on_connect(client, userdata, flags, rc):
    print('connected to jetson')

def on_connect_cloud(client, userdata, flags, rc):
    print('connected to cloud')

def on_message(client,userdata, msg):
    print('on message received')
    cloudmqttclient.publish(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)

mqttclient = mqtt.Client()
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.on_connect = on_connect

mqttclient.subscribe(MQTT_TOPIC, qos=2)
mqttclient.on_message = on_message

cloud_mqttclient = mqtt.Client()
cloud_mqttclient.on_connect = on_connect_cloud
cloud_mqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)


local_mqttclient.loop_forever()
