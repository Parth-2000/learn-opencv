import numpy as np
import cv2 as cv

# img = cv.imread("lena.jpg", 1)

img = np.zeros([500, 500, 3], np.uint8)


line = cv.line(img, (0, 0), (100, 100), (255, 255, 255), 2, cv.LINE_4)
arrowline = cv.arrowedLine(img, (0, 0), (10, 100), (0, 0, 255), 5, cv.LINE_AA)
rect = cv.rectangle(img, (100, 100), (300, 300), (0, 255, 0), -1)
circle = cv.circle(img, (300, 300), 100, (255, 0, 0), 5)
text = cv.putText(img, "OpenCV", (0, 300), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 3, cv.LINE_AA)
cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()
