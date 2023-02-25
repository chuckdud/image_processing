import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

side = ""

while(True):
    # take each frame
    _, frame = vid.read()
    frame = cv.blur(frame, (10, 10))

    # convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of yellow color in HSV
    lower_yellow = np.array([10,100,100])
    upper_yellow = np.array([40,255,255])

    
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    #get height of image
    height = mask.shape[0]
    height_cutoff = height // 2
    # get width of image
    width = mask.shape[1]
    width_cutoff = width // 2

    #left = mask[:, :width_cutoff]
    #right = mask[:, width_cutoff:]

    #total = np.sum(mask, dtype=np.int64)
    #l_count = np.sum(left, dtype=np.int64)
    #r_count = np.sum(right, dtype=np.int64)

    #l_dom = l_count > r_count
    #diff = abs(l_count - r_count)

    #if diff <= (total * .2):
    #    side = "mid"
    #elif l_dom:
    #    side = "left"
    #else:
    #    side = "right"
    #
    #print(side)

    #cv.imshow('Left mask', left)
    #cv.imshow('Right mask', right)

    M = cv.moments(mask)

    vertical = ""
    horical = ""

    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        if cX <= width_cutoff:
            horizontal = "left"
        else:
            horizontal = "right"

        if cY <= height_cutoff:
            vertical = "top"
        else:
            vertical = "bottom"

        cv.circle(mask, (cX,cY), 5, (0, 0, 0), -1)
        cv.putText(mask, horizontal + ", " + vertical, (cX - 25, cY - 25),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    cv.imshow("Mask", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv.destroyAllWindows()

