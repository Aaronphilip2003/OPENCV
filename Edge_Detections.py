import cv2 as cv
import numpy as np

def rescale(frame,scale=0.15):
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread("CAT.jpg")
resize=rescale(img)

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)

# cv.imshow("GRAY",gray)


#Laplacian Edge Detection

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("LAPLACIAN",lap)


#Sobel edge Detection

sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined=cv.bitwise_or(sobelx,sobely)
canny=cv.Canny(resize,100,100)

# cv.imshow("SOBEL-X",sobelx)
# cv.imshow("SOBEL-Y",sobely)
cv.imshow("COMBINED-SOBELS",combined)
cv.imshow("CANNY",canny)
#Combining Sobels



cv.waitKey(0)