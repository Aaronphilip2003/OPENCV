# importing libraries
import cv2
import numpy as np

# reading image
img = cv2.imread("DSC_1958.png")

def rescaleFrame(frame, scale = 0.20):
    width= int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =(width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)

# Cartoonization
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
#cv2.imshow("Image", img)
#cv2.imshow("edges", edges)
Resized_Edge=rescaleFrame(edges)
cv2.imshow("Edges Resized", Resized_Edge)
cv2.imshow("Cartoon", cartoon)
Resized_Cart=rescaleFrame(cartoon)
cv2.imshow("Cartoon Resized",  Resized_Cart)
cv2.waitKey(0)
cv2.destroyAllWindows()