import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')

# Painting
# blank[50:150, 150:250]=255,255,45
# #
# cv.imshow("Blank",blank)

#1.Rectangle

cv.rectangle(blank, (0,0), (250,250), (255,255,45),thickness=-2 )
cv.imshow("Blank",blank)

#2. Circle

cv.circle(blank,(250,250),100,(0,0,255),thickness=-1)
cv.imshow("Circle",blank)

#3.Ellipse

cv.ellipse(blank,(250,250),(100,200),90,0,360,(0,0,255),-1)
cv.imshow("Ellipse",blank)

#4. Putting text

cv.putText(blank,"Aaron Philip",(200,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)

cv.waitKey(0)