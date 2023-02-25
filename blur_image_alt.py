import cv2 as cv
import numpy as np

img = cv.imread("./test_image.jpg")

if img is None:
    sys.exit("Could not read the image.")

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

cv.imshow('Original', img)
cv.imshow('Averaging', dst)

cv.waitKey(0)
