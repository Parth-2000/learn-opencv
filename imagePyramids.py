import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("lena.jpg")

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    # cv.imshow(str(i), layer)

layer = gp[5]
cv.imshow("upper layer Gaussian Pyramid", layer)

lp = [layer]

for i in range(5, 0, -1):
    gaussianExtended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussianExtended)
    cv.imshow(str(i), laplacian)




# Gaussian Pyramid
# lr = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr)
# ur = cv.pyrUp(img)
#
# cv.imshow("Original Image", img)
# cv.imshow("Pyramid Down", lr)
# cv.imshow("Pyramid Down 2", lr2)
# cv.imshow("Pyramid Up", ur)


cv.waitKey(0)
cv.destroyAllWindows()

