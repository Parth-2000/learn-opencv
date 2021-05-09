import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Low Pass Filter helps in removing noise and blurring the image
# High Pass Filter helps in finding edges in the images

# img = cv.imread("opencv-logo.png")
# img = cv.imread("starry_night.jpg")
# img = cv.imread("water.png")
img = cv.imread("lena.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), dtype=np.float32) / 25

dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gaussianblur = cv.GaussianBlur(img, (5, 5), 0)
medianblur = cv.medianBlur(img, 5) # To remove salt and pepper noise
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)


titles = ["image", "2D Convolution", "Blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
images = [img, dst, blur, gaussianblur, medianblur, bilateralFilter]

for i in range(len(titles)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


cv.waitKey(0)

cv.destroyAllWindows()
