import cv2 as cv

img=cv.imread("ELON.jpg")

def rescale(frame,scale=.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


newimg=rescale(img)
# cv.imshow("ELON",newimg)

gray=cv.cvtColor(newimg,cv.COLOR_BGR2GRAY)
cv.imshow("IMAGE",gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'Number of Faces found = {len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(newimg,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("DETECTED FACES",newimg)
cv.waitKey(0)