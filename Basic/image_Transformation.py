import cv2 as cv
import numpy as np

a=cv.imread("E:/openCVtest/res/Berserk.png")
img=cv.resize(a,(a.shape[1]//4,a.shape[0]//4)) #img resize
cv.imshow("img",img)

'''the float create a tranMAt 2X3 row =[1,0,x] column=[0,1,y]'''
def translate(img,x,y):
    tranMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])     #it create a blank spcae so if you tanpose again it leaves blank spce
    return cv.warpAffine(img,tranMat,dimension)
trans=translate(img,100,100)
cv.imshow("Trans",trans)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

"""this rotation is done bv openCV we need to pass the correct parameter"""
def rotation(img,angle,rotpoint=None):
    width,height=img.shape[1],img.shape[0] #aimension
    if rotpoint is None:
        rotpoint=(width//2,height//2)   #center point
    point=cv.getRotationMatrix2D(rotpoint,angle,1.0)#  like the transMat in up def(if we didnt use this we manually do the math(its complicated)
    return cv.warpAffine(img,point,(width,height))
rot=rotation(img,-45)
cv.imshow("rotated",rot)

flip=cv.flip(img,0)# 1 -1 0
cv.imshow("filped",flip)

"""crop"""
cp=img[100:400,100 : 400]
cv.imshow("cropped", cp)

cv.waitKey(0)
