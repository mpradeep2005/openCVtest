import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

#colour change
blank[:]=0,0,100

#line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,200,2),9)
cv.imshow("line",blank)

#circle
ph=cv.imread("E:/openCVtest/photo/Berserk.png")
cv.circle(ph,(250,250),80,(200,0,0),-1)
cv.imshow("circle",ph)

#Rectangel
cv.rectangle(blank,(0,0),(250,250),(0,200,200),-1)
cv.imshow("rectangle",blank)

#Text
cv.putText(blank,"hi im pradeep",(0,100),cv.FONT_HERSHEY_COMPLEX_SMALL,1.0,(0,100,100),2)
cv.imshow("name",blank)

cv.waitKey(0)