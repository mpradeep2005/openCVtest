import cv2 as cv
"""0 means webcam or any path you can put like the """
capture=cv.VideoCapture(0)

while True:
    isTrue,frame=capture.read()
    cv.imshow("win",frame)
    if cv.waitKey(10) & 0xFF==ord("d"):# this is when user type d to exit
        break
capture.release()
cv.destroyAllWindows()