import cv2 as cv

vid=cv.VideoCapture(0)

haar=cv.CascadeClassifier("E:/openCVtest/res/haar_cas.xml")
while True:
    is_true,frame=vid.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    dec=haar.detectMultiScale(gray,1.1,3)
    for (x,y,w,h) in dec:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,200),3)
    cv.imshow("img",frame)
    if cv.waitKey(10) and 0xFF==ord('q'):
        break
vid.release()
cv.destroyAllWindows()