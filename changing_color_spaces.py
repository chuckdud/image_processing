import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

while(True):
    # take each frame
    _, frame = vid.read()
    frame = cv.blur(frame, (10, 10))

    # convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,2555,255])

    # define range of yellow color in HSV
    lower_yellow = np.array([10,100,100])
    upper_yellow = np.array([40,255,255])

    # threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    
    mask2 = cv.inRange(hsv, lower_yellow, upper_yellow)

    b_y_mask = cv.bitwise_or(mask1, mask2)
    # bitwise AND mask and original image
    res = cv.bitwise_and(frame, frame, mask = b_y_mask)

    cv.imshow('Original', frame)
    cv.imshow('Blue mask', mask1)
    cv.imshow('Yellow mask', mask2)
    cv.imshow('Combined mask', b_y_mask)
    cv.imshow('res', res)


    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv.destroyAllWindows()

