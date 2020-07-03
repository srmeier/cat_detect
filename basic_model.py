import warnings
warnings.simplefilter("ignore", UserWarning)

import cv2 as cv
import requests
from fastai.vision import *
from fastai.metrics import error_rate
import torch
from fastai.vision import Image
import matplotlib.pyplot as plt

learn = load_learner('data')
# faceCascade = cv.CascadeClassifier('haarcascade_frontalcatface.xml')
cap = cv.VideoCapture('http://raspberrypi.mshome.net:8000/stream.mjpg')

while True:
    ret, frame = cap.read()
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #img = Image(1 - torch.tensor(np.ascontiguousarray(np.flip(frame, 2)).transpose(2,0,1)))
    #data = ImageList.from_folder(mnist).split_by_folder().label_from_folder().add_test_folder('test').transform(tfms, size=32).databunch().normalize(imagenet_stats)
    #img.apply_tfms()
    img = Image(pil2tensor(frame, np.float32).div_(225))

    #print(img)
    pred = learn.predict(img, thresh=0.6)
    print(pred[0], pred[2][pred[1].item()])
    #print(learn.data.classes[pred[0][0]])
    
    cat_found = False
    # for (x, y, w, h) in faces:
    #     cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #     cat_found = True
    #cv.imshow('frame', frame)
    ax = plt.subplot()
    img.show(ax=ax)
    plt.show()
    #plt.imshow(img)
    break
    
    if cat_found:
        requests.get('http://raspberrypi.mshome.net:8000/see_cat')

    if (cv.waitKey(1) & 0xFF) == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break
