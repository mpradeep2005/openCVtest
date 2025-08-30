import cv2 as cv
from numpy.ma.extras import median

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
cv.imshow("noraml",img)
g_blur=cv.GaussianBlur(img,(9,9),0)
cv.imshow("Gaussian Blur",g_blur)       #mostly used take the weight of the surrounding pixels

blur=cv.blur(img,(9,9),0)
cv.imshow("blur",blur)                 #avg_blur take the avg of the surrounding pixel in the kernel


median_blur=cv.medianBlur(img,9)
cv.imshow("median_blur",median_blur)  #better than avg blur

b_filter=cv.bilateralFilter(img,15,50,5)
cv.imshow("Bilateral Filter",b_filter)  #used for face. IT is edge aware
cv.waitKey(0)