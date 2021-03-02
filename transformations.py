import cv2 as cv
import numpy as np

def rescale(frame, scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread("CAT.jpg")
resize=rescale(img)
cv.imshow("CAT",resize)

#Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(resize,100,100)

cv.imshow("Translated",translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(resize,45)
cv.imshow("Rotated",rotated)

cv.waitKey(0)