import numpy as np
import cv2
import paho.mqtt.client as mqtt

MQTT_HOST = 'nx_broker'

MQTT_PORT = 1883
MQTT_TOPIC = 'hw3'

def on_connect(client, userdata, flags, rc):
    print('connected with result code {0}'.format(str(rc)))

mclient = mqtt.Client()
mclient.on_connect = on_connect

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#could be something other than 0 depending on camera
cap = cv2.VideoCapture(0)

while(True):
    #get frame by frame captures
    ret, frame = cap.read()

    #operations on the frame go here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print('face detected', face.shape, face.dtype)
        rc, jpg = cv.lmencode(*png, face)
        msg = jpg.tobytes()
        mclient.publish(MQTT_TOPIC, payload = msg, qos = 2, retain = False)

    #display the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the captures
cap.release()
cv2.destroyAllWindows()
