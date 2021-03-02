import cv2 as cv

def rescale(frame, scale=0.25):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img=cv.imread("CAT.jpg")
resize=rescale(img)

cv.imshow("Cat",resize)

#Converting to Greyscale
# gray=cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
# cv.imshow("Grey",gray)


#Blurring Images
# blur=cv.GaussianBlur(resize,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

#Canny Edges

canny=cv.Canny(resize,125,175)
cv.imshow("Canny",canny )



cv.waitKey(0)