import cv2 as cv
import numpy as np

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
cv.imshow("noraml",img)
# The blank(mask) size should be same as the normal
blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("balnk",blank)

Rectangle=cv.rectangle(blank.copy(),(100,100),(400,400),250,-1)
circle=cv.circle(blank.copy(),(350,200),100,250,-1)

"""" for the masking we use Bitwise operator"""
mask_img=cv.bitwise_or(Rectangle,circle)

""" Mask the img,img with the mask"""
masked=cv.bitwise_and(img,img,mask=mask_img)
cv.imshow("masked",masked)

cv.waitKey(0)