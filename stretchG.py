import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("testImages/groundTruths/eg1_lowcntrst.jpg", 0)

# Create zeros array to store the stretched image
minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
print(minmax_img)

# Loop over the image and apply Min-Max formulae
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        minmax_img[i, j] = (img[i, j] - np.min(img)) / (np.max(img) - np.min(img))

# Displat the stretched image
cv.imshow("Minmax", minmax_img)
cv.waitKey(0)
