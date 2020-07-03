import warnings
warnings.simplefilter("ignore", UserWarning)

import cv2 as cv
import requests
from fastai.vision import *
from fastai.metrics import error_rate
from fastai.vision import Image
from time import sleep
import numpy as np



learn = load_learner('data')
cap = cv.VideoCapture('http://raspberrypi.mshome.net:8000/stream.mjpg')

i = 20
j = 0
preds_array = [''] * 3

while True:
    ret, frame = cap.read()

    if i > 0:
        i -= 1
        continue
    i = 20

    pred = learn.predict(Image(pil2tensor(np.flip(frame, 2), np.float32).div_(225)))
    pred_cat = str(pred[0])
    pred_prob = float(pred[2][pred[1].item()])

    if (pred_prob > .8) and ((pred_cat == 'java') or (pred_cat == 'python')):
        pred = pred_cat
    else:
        pred = ''
    preds_array[j % 3] = pred
    j += 1
    
    cat_found = False
    print(np.array(preds_array), pred_prob, pred_cat)
    if np.all(np.array([cat == pred_cat for cat in preds_array])):
        cat_found = True
    
    if cat_found:
        requests.get('http://raspberrypi.mshome.net:8000/see_cat')

    cv.imshow('frame', frame)
    if (cv.waitKey(1) & 0xFF) == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break
