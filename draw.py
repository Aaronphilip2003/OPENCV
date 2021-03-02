import cv2 as cv
import numpy as np

def rescale(frame,scale=0.25):
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

img = cv.imread("CAT.jpg")

size_Corrector=rescale(img)

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank",blank)

#Paint
blank[200:300, 300:400]=0,255,0
cv.imshow("Green",blank)


cv.imshow("Cat",size_Corrector)

cv.waitKey(0)