import cv2 as cv

img=cv.imread("E:/openCVtest/res/Berserk.png")
cv.imshow("img",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#simple Threshold
thres,simp_thre=cv.threshold(gray,100,255,cv.THRESH_BINARY,)
cv.imshow("Simple_Thresholding" , simp_thre)

#simple inverse
thres,simple_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow("simple_inv",simple_inv)

#adaptive threshold
Adap_thres=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,10)#10 is subtracted with the mean value
cv.imshow("Adaptive Threshold",Adap_thres)
cv.waitKey(0)
"""
🔑 Thresholding in OpenCV – Key Notes
1. Grayscale Conversion

Thresholding works best on single-channel images.

Use:

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

2. Simple Thresholding (cv.threshold)

Syntax:

ret, thresh = cv.threshold(src, thresh_value, max_value, type)


Parameters:

thresh_value: cutoff value (e.g., 100)

max_value: value assigned if condition passes (usually 255)

type: method used (THRESH_BINARY, THRESH_BINARY_INV, etc.)

Result:

Pixels < threshold → 0

Pixels >= threshold → max_value

3. Simple Inverse Thresholding (THRESH_BINARY_INV)

Opposite of THRESH_BINARY:

Pixels < threshold → max_value

Pixels >= threshold → 0

4. Adaptive Thresholding (cv.adaptiveThreshold)

Threshold is calculated per pixel based on neighborhood values.

Useful for images with uneven lighting.

Parameters:

max_value: usually 255

adaptiveMethod:

ADAPTIVE_THRESH_MEAN_C → mean of neighborhood − constant C

ADAPTIVE_THRESH_GAUSSIAN_C → weighted mean (Gaussian) − constant C

blockSize: neighborhood size (must be odd, e.g., 9)

C: constant subtracted (e.g., 10)

5. Return Values

ret: threshold value used (only for simple threshold).

thresh: the resulting thresholded image."""