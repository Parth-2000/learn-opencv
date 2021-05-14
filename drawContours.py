import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("sudoku.png")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("No of Contours: " + str(len(contours)))
# print(contours)

cv.drawContours(img, contours, 10, (0, 255, 255), 3)



cv.imshow("Image", img)
cv.imshow("Image Gray", imgray)


cv.waitKey(0)
cv.destroyAllWindows()

