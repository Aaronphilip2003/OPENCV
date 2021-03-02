import cv2 as cv
import matplotlib.pyplot as plt

def rescale(frame,scale=0.15):
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread("CAT.jpg")
resize=rescale(img)

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)

cv.imshow("GRAY",gray)

#GRAYSCALE HISTOGRAM

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('GRAYSCALE HISTOGRAM')
plt.xlabel('BINS')
plt.ylabel('NO. OF PIXELS')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#COLOUR HISTOGRAM
plt.title('COLOUR HISTOGRAM')
plt.xlabel('BINS')
plt.ylabel('NO. OF PIXELS')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([resize],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)