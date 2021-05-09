import cv2 as cv
import numpy as np

img = cv.imread("messi5.jpg", 1)
img_2 = cv.imread("opencv-logo.png", 1)

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

ball = img[280:340, 330:390]

img[273:333, 100:160] = ball
img = cv.resize(img, (512, 512))
img_2 = cv.resize(img_2, (512, 512))
add = cv.add(img, img_2)
add_weighted = cv.addWeighted(img, 1, img_2, 0.3, 0)

cv.imshow("Add", add)
cv.imshow("Add Weighted", add_weighted)

cv.imshow("Ball", ball)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
