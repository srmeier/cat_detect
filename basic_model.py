import cv2 as cv
import requests

faceCascade = cv.CascadeClassifier('haarcascade_frontalcatface.xml')
cap = cv.VideoCapture('http://192.168.137.225:8000/stream.mjpg')

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    cat_found = False
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cat_found = True
    cv.imshow('frame', frame)
    
    if cat_found:
        requests.get('http://192.168.137.225:8000/see_cat')

    if (cv.waitKey(1) & 0xFF) == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break
