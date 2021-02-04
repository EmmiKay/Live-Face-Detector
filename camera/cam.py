import numpy as np
import cv2
import paho.mqtt.client as mqtt
import os
import time

MQTT_BROKER = 'nx_broker'
MQTT_PORT = 1883
MQTT_TOPIC = 'hw3'

def on_connect_local(client, userdata, flags, rc): 
    print("connected to local broker with rc: " + str(rc))
    main()

def main():
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
            print('face detected', frame.shape, frame.dtype)
            rc, png = cv2.imencode('.png', frame)
            msg = png.tobytes()
            mqttclient.publish(MQTT_TOPIC, payload = msg, qos = 0, retain = False)
        #display the frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #release the captures
    cap.release()

if __name__ == '__main__':
    mqttclient = mqtt.Client()
    mqttclient.on_connect = on_connect_local
    mqttclient.connect(MQTT_BROKER, MQTT_PORT, 60)

    mqttclient.loop_forever()
    cv2.destroyAllWindows()
