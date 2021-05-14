import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("gradient.png")
_, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ["Image", "Threshold Binary", "Threshold Binary Inverse", "Threshold Trunk", "Threshold To Zero", "Threshold To Zero Inverse"]
images = [img, thresh, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# cv.imshow("Image", img)
# cv.imshow("Threshold Binary", thresh)
# cv.imshow("Threshold Binary Inverse", thresh2)
# cv.imshow("Threshold Trunk", thresh3)
# cv.imshow("Threshold To Zero", thresh4)
# cv.imshow("Threshold To Zero Inverse", thresh5)
cv.waitKey(0)
cv.destroyAllWindows()