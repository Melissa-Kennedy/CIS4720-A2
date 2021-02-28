import cv2 as cv
import numpy as np

def image_quality(filename1, filename2):
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    M = len(img1)
    Q = 0

    for i in range(M):
        N = len(img1[i])
        mean_x = np.mean(img1[i])
        mean_y = np.mean(img2[i])

        variance_x = sum([(pixel - mean_x) ** 2 for pixel in img1[i]]) / N - 1
        variance_y = sum([(pixel - mean_y) ** 2 for pixel in img2[i]]) / N - 1

        sigma_xy = sum([(img1[i][j] - mean_x)*(img2[i][j] - mean_y) for j in range(len(img2[i]))]) / N - 1

        Q += (4 * sigma_xy * mean_x * mean_y) / ((variance_x + variance_y) * ((mean_x ** 2) + (mean_y ** 2)))

    return Q / M
