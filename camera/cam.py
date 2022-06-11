import numpy as np
import cv2 as cv
import time
import paho.mqtt.client as mqtt

#open the camera for video captuer
cap = cv.VideoCapture(0)

#face finder
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#start mqtt messaging client
client = mqtt.Client()

def face(frame):
    '''locate and clip faces in each video frame'''
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    #cut out faces and convert to png
    for (x,y,w,h) in faces:
        face = frame[y:y+h, x:x+w]

        rc,png = cv.imencode('.png', face)
        face = png.tobytes()
        pub_face(face)

def pub_face(face):
    '''connect to broker and publish face image'''
    client.connect("nx_broker",1883,60)
    client.publish("hw3", payload=face, qos=1, retain=False);
    client.disconnect();

#run the code continuously
while(True):
    #ret - boolean returns true if frame is available, frame - array vector of the image
    ret, frame = cap.read()

    #clip and publish the recognized faces
    face(frame)
