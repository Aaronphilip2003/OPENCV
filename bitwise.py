import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

# cv.imshow("RECTANGLE",rectangle)
# cv.imshow("CIRCLE",circle)

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("BITWISE",bitwise_and)

bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("BITWISE2",bitwise_or)

bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("BITWISE3",bitwise_xor)

bitwise_not=cv.bitwise_not(rectangle,circle)
cv.imshow("BITWISE3",bitwise_not)


cv.waitKey(0)