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

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("BLUR",blur)
#
# canny=cv.Canny(resize,50,50)
# cv.imshow("Canny",canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("THRESH",thresh)

contours,heirarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} found ')



cv.waitKey(0)