import cv2 as cv
#Rescale Function
def rescale(frame, scale=2.00):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)




img =cv.imread("IMG_4657.JPG")
resize=rescale(img)

cv.imshow("resized",resize)
#cv.imshow("Ryan",img)

cv.waitKey(0)