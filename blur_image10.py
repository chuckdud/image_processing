import cv2 as cv

img = cv.imread("./test_image.jpg")

if img is None:
    sys.exit("Could not read the image.")

window_name = 'Image'

ksize = (10, 10)

img = cv.blur(img, ksize)

cv.imshow(window_name, img)

k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("blurred10.jpg", img)
