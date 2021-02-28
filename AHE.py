import cv2 as cv

def ahe(filename):
    img = cv.imread(filename, 0)
    ahe = cv.createCLAHE(clipLimit=0, tileGridSize=(9, 9))
    ahe_img = ahe.apply(img)

    cv.imwrite("editedImages/adaptive_histogram_equalization.png", ahe_img)