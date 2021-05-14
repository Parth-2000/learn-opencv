import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
dilation = cv.dilate(mask, kernel=kernel, iterations=2)
erosion = cv.erode(mask, kernel=kernel, iterations=1)
# Opening -> First Erosion will be applied and then Dilation
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel=kernel)
# Closing -> First Dilation will be applied and then Erosion
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel=kernel)
morphgradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel=kernel)
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel=kernel)
blackhat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernel=kernel)

titles = ["Image", "mask", "dilation", "erosion", "opening", "closing", "morphgradient", "tophat", "blackhat"]
images = [img, mask, dilation, erosion, opening, closing, morphgradient, tophat, blackhat]

for i in range(len(titles)):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

