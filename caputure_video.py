import cv2 as cv

vid = cv.VideoCapture(0)

while(True):
    # Capture video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv.imshow('frame', frame)

    # 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop, release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
