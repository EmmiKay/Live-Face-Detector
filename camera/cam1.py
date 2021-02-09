import numpy as np
import cv2 as cv2
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = 'nx_broker'
MQTT_PORT = 1883
MQTT_TOPIC = 'hw3'

cap = cv2.VideoCapture(0)

face_cascade = cv.CascadeClassifier('/face_detect/haarcascades/haarcascade_frontalface_default.xml')
client = mqtt.Client()

def get_face(frame):
    gray = cv.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print('face detected', frame.shape, frame.dtype)
        rc, png = cv2.imencode('.png', frame)
        msg = png.tobytes()
        publish_face(msg)


def publish_face(face):
    client.connect("nx_broker",1883,60)
    client.publish("hw3", payload=msg, qos=1, retain=False);
    client.disconnect();

while(True):
    ret, frame = cap.read()
    get_face(frame)
