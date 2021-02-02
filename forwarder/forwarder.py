import paho.mqtt.client as mqtt

MQTT_HOST = 'nx_broker'
#MQTT_HOST = '73.101.143.198'
MQTT_PORT = 1883
MQTT_TOPIC = "hw3"

#CLOUD_MQTT_HOST = '18.221.177.196'
CLOUD_MQTT_HOST = 'ec2-18-224-93-123.us-east-2.compute.amazonaws.com'
CLOUD_MQTT_PORT = 1883
CLOUD_MQTT_TOPIC = 'faces'

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    mqttclient.subscribe(MQTT_TOPIC)

def on_connect_cloud(client, userdata, flags, rc):
        print('connected to cloud')

def on_message(client,userdata, msg):
    try:
        print('on message received')
        msg = msg.payload
        cloudmqttclient.publish(CLOUD_MQTT_TOPIC, payload=msg, qos=1, retain=True)
        print('message published!')
    except:
        print("Unexpected error:", sys.exc_info()[0])

mqttclient = mqtt.Client()
mqttclient.connect(MQTT_HOST, MQTT_PORT, 60)
mqttclient.on_connect = on_connect_local

cloud_mqttclient = mqtt.Client()
cloud_mqttclient.connect(CLOUD_MQTT_HOST, CLOUD_MQTT_PORT, 60)
cloud_mqttclient.on_connect = on_connect_cloud

mqttclient.on_message = on_message

mqttclient.loop_forever()
