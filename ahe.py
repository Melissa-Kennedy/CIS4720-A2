import cv2 as cv

def ahe(filename):
    # Read the image
    img = cv.imread(filename, 0)

    # Run the CLAHE function with no clip limit. This is the same as AHE
    ahe = cv.createCLAHE(clipLimit=0, tileGridSize=(9, 9))
    ahe_img = ahe.apply(img)

    # Save the image
    cv.imwrite("editedImages/adaptive_histogram_equalization.jpg", ahe_img)
