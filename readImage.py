import cv2 as cv

img = cv.imread("lena.jpg", 0)

print(img.shape[::-1])

cv.imshow("Image", img)

cv.waitKey(0) & 0xFF

cv.destroyAllWindows()

cv.imwrite("lena_copy.jpg", img)
