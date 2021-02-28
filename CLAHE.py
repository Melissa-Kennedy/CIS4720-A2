import cv2 as cv

def clahe(filename):
    img = cv.imread(filename, 0)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(9, 9))
    clahe_img = clahe.apply(img)

    cv.imwrite("editedImages/contrast_limited_adaptive_histogram_equalization.png", clahe_img)