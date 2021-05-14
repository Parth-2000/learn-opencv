import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)
# fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)


while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow("Frame", frame)
    cv.imshow("FG MASK Frame", fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == "q" or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()
