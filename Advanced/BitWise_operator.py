import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype="uint8")

rectangle=cv.rectangle(blank.copy(),(100,100),(400,400),250,-1)
cv.imshow("rec",rectangle)

circle=cv.circle(blank,(250,250),170,250,-1)
cv.imshow("circle",circle)

"""Bitwise AND"""
And=cv.bitwise_and(rectangle,circle)
cv.imshow("AND",And)

"""Bitwsise OR"""
Or=cv.bitwise_or(rectangle,circle)
cv.imshow("OR",Or)

"""BitWise Xor"""
xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("Xor",xor)

"""BitWise Not"""
Not=cv.bitwise_not(circle)
cv.imshow("NOT",Not)

cv.waitKey(0)