import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("lena.jpg")

cv.imshow("Image", img)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

