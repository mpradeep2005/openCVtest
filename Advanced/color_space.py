import cv2 as cv

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
cv.imshow("img",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)               #we cannot change directly from Lab to HSV
cv.imshow("HSV",hsv)                        #First we need to change it to gbr

lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("LAB", lab)

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)               #the color formate is GBR not RGB in openCV
cv.imshow("RGB",rgb)

cv.waitKey(0)