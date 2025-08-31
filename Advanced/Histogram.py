import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np



img=cv.imread("E:/openCVtest/res/AOT.jpeg")
cv.imshow("img",img)
#mask

#GrayScale Histogram
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])


plt.figure()
plt.title("gray histogram")
plt.xlabel("bin")
plt.ylabel("no of pixel")
plt.plot(gray_hist)
plt.xlim([0,256])#x axis limiter


"""Imagine you’re counting how many students got each score from 0 to 100 in a test:

X-axis = score

Y-axis = number of students

Same idea here:

X-axis = brightness

Y-axis = number of pixels"""

blank=np.zeros(img.shape[:2],dtype="uint8")                              #use white color in blank
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_or(img,img,mask=circle)
cv.imshow("masked",masked)

plt.figure()# create a blank sheet if not created it overwrite on a single sheet
plt.title("Color histogram")
plt.xlabel("Bin")
plt.ylabel("no of pixel")

"""take i as 0,1,2 and col as 'b','g','r' """
colors=('b','g','r')
for i,col in enumerate(colors):
    color_hist=cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(color_hist,color=col)
plt.show()# should be one show or if you use two after closing one only another opens

cv.waitKey(0)
