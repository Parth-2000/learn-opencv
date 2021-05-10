import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.jpg")

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
# b, g, r = cv.split(img)

# img = np.zeros((200, 200), dtype=np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 100), (200, 150), (127), -1)


# cv.imshow("Image", img)
# cv.imshow("B", b)
# cv.imshow("G", g)
# cv.imshow("R", r)


# plt.hist(img.ravel(), 256, [0, 256])
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])

plt.show()



cv.waitKey(0)
cv.destroyAllWindows()

