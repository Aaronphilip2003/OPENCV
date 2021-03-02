import cv2 as cv

def rescale(frame, scale=.15):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img =cv.imread("CAT.jpg")
resize=rescale(img)

cv.imshow("Resize",resize)

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY",gray)

#BGR to HSV
hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

#BGR to LAB

lab=cv.cvtColor(resize,cv.COLOR_BGR2Lab)
cv.imshow("LAB",lab)

cv.waitKey(0)