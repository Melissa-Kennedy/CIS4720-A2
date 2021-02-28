import cv2 as cv

def clahe(filename):
    # Read the image
    img = cv.imread(filename, 0)

    # Run OpenCV's CLAHE function
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(9, 9))
    clahe_img = clahe.apply(img)

    # Save the image
    cv.imwrite("editedImages/contrast_limited_adaptive_histogram_equalization.jpg", clahe_img)