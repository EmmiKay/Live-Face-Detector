import paho.mqtt.client as mqtt

#MQTT_HOST = '73.1011.143.198'
MQTT_HOST = 'emily-desktop'
MQTT_PORT = 1883
MQTT_TOPIC = 'hw3'

#CLOUD_MQTT_HOST = '18.221.177.196'
CLOUD_MQTT_HOST = 'ec2-18-221-177-196.us-east-2.compute.amazonaws.com'
CLOUD_MQTT_PORT = 1883
CLOUD_MQTT_TOPIC = 'faces'

def on_connect(client, userdata, flags, rc):
    print('Connected to Jetson')

def on_connect_cloud(client, userdata, flags, rc):
    print('Connected to cloud')

def on_message(client, userdata, flags, rc):
    print('on message received')
    cloudmqttclient.publish(CLOUD_MQTT_TOPIC, payload = msg.payload, qos = 2, retain = False)

cloudmqttclient = mqtt.Client()
cloudmqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)
cloudmqttclient.on_connect = on_connect_cloud

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message

mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.subscribe(MQTT_TOPIC, qos = 2)

mqttclient.loop_foreer()
