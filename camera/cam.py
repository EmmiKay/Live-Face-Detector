import numpy as np
import cv2 as cv
import time
import paho.mqtt.client as mqtt

cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
client = mqtt.Client()

def face(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]

        rc,png = cv.imencode('.png', face)
        face = png.tobytes()
        pub_face(face)

def pub_face(face):
    client.connect("nx_broker",1883,60)
    client.publish("hw3", payload=face, qos=1, retain=False);
    client.disconnect();

while(True):
    ret, frame = cap.read()
    face(frame)
