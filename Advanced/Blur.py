import cv2 as cv

img=cv.imread("E:/openCVtest/res/AOT.jpeg")
cv.imshow("noraml",img)
g_blur=cv.GaussianBlur(img,(9,9),0)
cv.imshow("Gaussian Blur",g_blur)

blur=cv.blur(img,(9,9),0)
cv.imshow("blur",blur)

avg_blur=cv.medianBlur(img,9)
cv.imshow("avg_blur",avg_blur)

b_filter=cv.bilateralFilter(img,15,50,5)
cv.imshow("Bilateral Filter",b_filter)
cv.waitKey(0)