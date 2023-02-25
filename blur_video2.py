import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

vid = cv.VideoCapture(0)

while(True):
    ret, frame = vid.read()

    kernel = np.ones((5,5), np.float32) / 25

#    dst = cv.blur(frame, (5,5))
#    dst = cv.filter2D(frame, -1, kernel)
    dst = cv.medianBlur(frame, 9)
#    dst = cv.GaussianBlur(frame, (5,5), 0)
#    dst = cv.bilateralFilter(frame, 9, 75, 75)

    cv.imshow('Original', frame)
    cv.imshow('Blurred', dst)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv.destroyAllWindows()
