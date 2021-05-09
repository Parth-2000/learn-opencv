import cv2 as cv
import numpy as np

# img = cv.imread("shapes.png")
img = cv.imread("shapes_test.jpg")

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img.shape)

_, thresh = cv.threshold(imgray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 255, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        # print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))




cv.imshow("image", img)
cv.imshow("gray", imgray)
cv.imshow("thresh", thresh)

cv.waitKey(0)
cv.destroyAllWindows()

