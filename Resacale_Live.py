import cv2 as cv

capture =cv.VideoCapture(0)

def setDim(width,height):
    capture.set(3,width)
    capture.set(3,height)

setDim(100,100)#permanatly change the resolution

while True:
    isTrue,frame=capture.read()
    cv.imshow("live",frame)

    if cv.waitKey(10) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
