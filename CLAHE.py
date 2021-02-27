import cv2 as cv

def clahe(filename):
    img = cv.imread(filename, 0)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(9, 9))
    clahe_img = clahe.apply(img)

    cv.imshow("Contrast Limited Adaptive Histogram Equalization.png", clahe_img)
    cv.waitKey(0)