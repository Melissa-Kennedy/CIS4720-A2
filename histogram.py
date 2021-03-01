import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Reading the original image, here 0 implies that image is read as grayscale
img = cv.imread("testImages/groundTruths/eg2_lowcntrst4.jpg", 0)

# Histogram before
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
plt.hist(img.flatten(), 256, [0, 256], color="r")
plt.xlim([0, 256])
plt.title("Histogram for Image 5")
plt.ylabel("Frequency")
plt.xlabel("Intensity")
plt.show()