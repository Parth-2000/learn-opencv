import cv2 as cv
import numpy as np

img = cv.imread("pic1.png")

cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, (0, 255, 0), -1)

cv.imshow("dst", img)

cv.waitKey(0)
cv.destroyAllWindows()