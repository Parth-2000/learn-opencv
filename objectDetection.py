import cv2 as cv
import numpy as np


def nothing(x):
    print(x)

cap = cv.VideoCapture(0)
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # frame = cv.imread("smarties.png")
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lh = cv.getTrackbarPos("LH", "Tracking")
    ls = cv.getTrackbarPos("LS", "Tracking")
    lv = cv.getTrackbarPos("LV", "Tracking")
    uh = cv.getTrackbarPos("UH", "Tracking")
    us = cv.getTrackbarPos("US", "Tracking")
    uv = cv.getTrackbarPos("UV", "Tracking")
    lb = np.array([lh, ls, lv])
    ub = np.array([uh, us, uv])
    mask = cv.inRange(hsv, lb, ub)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()
