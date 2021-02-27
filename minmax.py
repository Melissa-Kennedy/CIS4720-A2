import cv2 as cv
import numpy as np

def minmax(filename):
    img = cv.imread(filename, 0)

    minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")

    min_pixel = np.min(img)
    max_pixel = np.max(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            minmax_img[i, j] = (img[i, j] - min_pixel) / (max_pixel - min_pixel) * 255

    cv.imshow("Minmax", minmax_img)
    cv.waitKey(0)
