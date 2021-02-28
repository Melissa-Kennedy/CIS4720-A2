import cv2 as cv
import numpy as np

def image_quality(filename1, filename2):
    # Read both images
    # One is editeed the other is the ground truth
    img1 = cv.imread(filename1, 0)
    img2 = cv.imread(filename2, 0)

    # Get M and initialize Q to q to start
    M = len(img1)
    Q = 0

    # Calculate Q_j
    for i in range(M):
        # Get N and the means of both images
        N = len(img1[i])
        mean_x = np.mean(img1[i])
        mean_y = np.mean(img2[i])

        # Get the variance for both images
        variance_x = sum([(pixel - mean_x) ** 2 for pixel in img1[i]]) / N - 1
        variance_y = sum([(pixel - mean_y) ** 2 for pixel in img2[i]]) / N - 1

        # Get sigma of both images
        sigma_xy = sum([(img1[i][j] - mean_x)*(img2[i][j] - mean_y) for j in range(len(img2[i]))]) / N - 1

        # Add Q_j to the total quality
        Q += (4 * sigma_xy * mean_x * mean_y) / ((variance_x + variance_y) * ((mean_x ** 2) + (mean_y ** 2)))

    # Average Q and return
    return Q / M
