import cv2 as cv
import numpy as np

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
blank=np.zeros(img.shape[:2],dtype='uint8') # [:2] means 2d without any color

B,G,R=cv.split(img)

print(G)
print(B)
print(R)

merge=cv.merge([B,G,R])
cv.imshow("merged",merge)

blue=cv.merge([B,blank,blank])
green=cv.merge([blank,G,blank])
red=cv.merge([blank,blank,R])

cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)