# import cv2
# from matplotlib import pyplot as plt


# def createHistogram(image):

# img = cv2.imread(image,0)
# plt.hist(image[:, :, 0].ravel(), bins=256, color='red', alpha=0.5)
# plt.hist(image[:, :, 1].ravel(), bins=256, color='green', alpha=0.5)
# plt.hist(image[:, :, 2].ravel(), bins=256, color='blue', alpha=0.5)
# plt.hist(img.ravel(),256,[0,256])
# plt.title(image)
# plt.show()

# img = cv2.imread(image)
# color = ("b", "g", "r")
# for i, col in enumerate(color):
# histr = cv2.calcHist([img], [i], None, [256], [0, 256])
# plt.plot(histr, color=col)
# plt.xlim([0, 256])
# plt.show()

# createHistogram("motion.png")
# createHistogram("noise.png")
# createHistogram("unfocused.png")
# createHistogram("overExposed.png")
# createHistogram("underExposed.png")
# createHistogram("wb.png")
# createHistogram("motionEdit(1).png")
# createHistogram("noiseEdited.png")
# createHistogram("unfocusedEdit.png")
# createHistogram("overExposedEdited.png")
# createHistogram("underExposedEdit8.png")
# createHistogram("wbEdit.png")

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Reading the original image, here 0 implies that image is read as grayscale
img = cv.imread("motion.png", 0)

# Histogram before
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color="b")
plt.hist(img.flatten(), 256, [0, 256], color="r")
plt.xlim([0, 256])
plt.legend(("cdf", "histogram"), loc="upper left")
# plt.show()

# equalize picture
equ = cv.equalizeHist(img)
# cv.imshow("equ.png", equ)
# cv.waitKey(0)

# Histo after

hist, bins = np.histogram(equ.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color="b")
plt.hist(equ.flatten(), 256, [0, 256], color="r")
plt.xlim([0, 256])
plt.legend(("cdf", "histogram"), loc="upper left")
# plt.show()

# clahe
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv.imshow("cl1.png", cl1)
cv.waitKey(0)