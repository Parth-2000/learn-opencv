import cv2 as cv
import numpy as np

img = cv.imread("sudoku.png", 0)
_, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
adaptivethresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
adaptivethresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Image", img)
cv.imshow("Threshold Image", thresh)
cv.imshow("Adaptive Threshold Image Mean", adaptivethresh)
cv.imshow("Adaptive Threshold Image Gaussian", adaptivethresh2)

cv.waitKey(0)
cv.destroyAllWindows()


