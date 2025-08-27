import cv2 as cv
import numpy as np

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
blank =np.zeros(img.shape,dtype='uint8')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,125,200)            # canny edge detector
res,thes=cv.threshold(gray,175,200,cv.THRESH_BINARY)
contour,hierarchies=cv.findContours(thes,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)# we can use thres or canny but canny is suggested
print(contour)
cv.drawContours(blank,contour,-1,(0,0,200),1)
cv.imshow("contour",blank)
cv.waitKey(0)