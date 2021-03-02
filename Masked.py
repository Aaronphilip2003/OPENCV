import cv2 as cv
import numpy as np


def rescale(frame, scale=.15):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img =cv.imread("CAT.jpg")
resize=rescale(img)

blank=np.zeros(resize.shape[:2],dtype='uint8')
# cv.imshow("Blank Image",blank)

mask=cv.circle(blank,(resize.shape[1]//2,resize.shape[0]//2),200,255,-1)
# cv.imshow("MASK",mask)

masked=cv.bitwise_and(resize,resize,mask=mask)
cv.imshow("MASKED IMAGE",masked)



cv.waitKey(0)