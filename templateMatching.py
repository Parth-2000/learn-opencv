import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("messi5.jpg")
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread("messi_template.jpg", 0)
w, h = template.shape[::-1]

# res = cv.matchTemplate(grey_img, template, cv.TM_CCOEFF_NORMED)
res = cv.matchTemplate(grey_img, template, cv.TM_CCORR_NORMED)
print(res)

threshold = 0.99
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)



print(loc)


cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
