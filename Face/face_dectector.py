import cv2 as cv

img=cv.imread("E:/openCVtest/res/download.jpeg")

haar_cascades=cv.CascadeClassifier("E:/openCVtest/res/haar_cas.xml")

face_rect=haar_cascades.detectMultiScale(img,1.1,1)
print(len(face_rect))

for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,200),3)
cv.imshow("img",img)
cv.waitKey(0)