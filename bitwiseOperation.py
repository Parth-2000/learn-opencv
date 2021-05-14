import cv2 as cv
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv.rectangle(img2, (0, 0), (250, 250), (255, 255, 255), -1)

# bitAnd = cv.bitwise_and(img2, img1)
# cv.imshow("BitAnd", bitAnd)

# bitOr = cv.bitwise_or(img2, img1)
# cv.imshow("BitOr", bitOr)

# bitXor = cv.bitwise_xor(img2, img1)
# cv.imshow("BitXor", bitXor)

# bitNot = cv.bitwise_not(img1)
# cv.imshow("BitNot", bitNot)

cv.imshow("Image1", img1)
cv.imshow("Image2", img2)

cv.waitKey(0)
cv.destroyAllWindows()



