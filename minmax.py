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

    cv.imwrite("editedImages/minmax.jpg", minmax_img)


def local_minmax(filename, radius):
    img = cv.imread(filename, 0)

    minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = i - radius if i - radius >= 0 else i
            h = i + radius + 1 if i + radius + 1 < img.shape[0] else i
            x = j - radius if j - radius >= 0 else j
            l = j + radius + 1 if j + radius + 1 < img.shape[0] else j

            min_pixel = np.min(img[y:h, x:l])
            max_pixel = np.max(img[y:h, x:l])
            
            minmax_img[i, j] = (img[i, j] - min_pixel) / (max_pixel - min_pixel) * 255

    cv.imwrite("editedImages/local_minmax.jpg", minmax_img)
