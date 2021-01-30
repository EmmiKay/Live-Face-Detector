import numpy as np
import cv2
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

    #display the frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the captures
cap.relese()
cv2.destroyAllWindows()
