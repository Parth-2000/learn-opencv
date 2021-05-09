# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# img = cv.imread("messi5.jpg", cv.IMREAD_GRAYSCALE)
#
# laplace = cv.Laplacian(img, cv.CV_64F, ksize=3)
# laplace = np.uint8(np.absolute(laplace))
#
# sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
# sobelY = np.uint8(np.absolute(sobelY))
#
# sobelCombined = cv.bitwise_or(sobelX, sobelY)
#
# canny = cv.Canny(img, 100, 200)
#
#
#
# # titles = ["image", "Laplacian Gradient", "Sobel X", "Sobel Y", "Sobel Combined"]
# # images = [img, laplace, sobelX, sobelY, sobelCombined]
#
# titles = ["image", "Canny"]
# images = [img, canny]
#
# for i in range(len(titles)):
#     plt.subplot(3, 2, i+1), plt.imshow(images[i], "gray")
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
#
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np


def nothing(x):
    pass


cv.namedWindow("image")

cv.createTrackbar('T1', "image", 0, 500, nothing)
cv.createTrackbar('T2', "image", 0, 500, nothing)

while True:
    img = cv.imread("messi5.jpg", cv.IMREAD_GRAYSCALE)


    T1 = cv.getTrackbarPos('T1', 'image')
    T2 = cv.getTrackbarPos('T2', 'image')
    canny = cv.Canny(img, T1, T2)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    cv.imshow("image", canny)

cv.destroyAllWindows()



