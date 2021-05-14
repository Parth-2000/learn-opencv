import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

# def click_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         print(x, "   ", y)
#         font = cv.FONT_HERSHEY_SIMPLEX
#         text = str(x) + " " + str(y)
#         cv.putText(img, text, (x, y), font, 0.5, (255, 255, 255), 2)
#         cv.imshow('Image', img)
#     if event == cv.EVENT_RBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         font = cv.FONT_HERSHEY_SIMPLEX
#         text_2 = str(blue) + " " + str(green) + " " + str(red)
#         cv.putText(img, text_2, (x, y), font, 0.5, (0, 255, 255), 2)
#         cv.imshow('Image', img)

# def click_event(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.circle(img, (x, y), 3, (0, 255, 255), -1)
#         points.append((x, y))
#         if len(points) > 1:
#             cv.line(img, points[-1], points[-2], (255, 0, 0), 5)
#         cv.imshow('Image', img)


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv.circle(img, (x, y), 3, (0, 255, 255), -1)
        colorImage = np.zeros((512, 512, 3), np.uint8)
        colorImage[:] = [blue, green, red]
        cv.imshow('Coloured Image', colorImage)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("lena.jpg", 1)
cv.imshow("Image", img)
points = []
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()
