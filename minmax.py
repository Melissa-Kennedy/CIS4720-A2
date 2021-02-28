import cv2 as cv
import numpy as np

def minmax(filename):
    # Read the image
    img = cv.imread(filename, 0)

    # Initialize an array of zeros to eventually write the new image to
    minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")

    # Calculate the min and max values of the histogram
    min_pixel = np.min(img)
    max_pixel = np.max(img)

    # Apply the formula to each pixel and write it to zero array
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            minmax_img[i, j] = (img[i, j] - min_pixel) / (max_pixel - min_pixel) * 255

    # Save the image
    cv.imwrite("editedImages/minmax.jpg", minmax_img)


def local_minmax(filename, radius):
    # Read the image
    img = cv.imread(filename, 0)

    # Initialize an array of zeros to eventually write the new image to
    minmax_img = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")

    # Apply the formula to each pixel after geting the min and max values around it
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Get the box surrounding each pixel
            y = i - radius if i - radius >= 0 else i
            h = i + radius + 1 if i + radius + 1 < img.shape[0] else i
            x = j - radius if j - radius >= 0 else j
            l = j + radius + 1 if j + radius + 1 < img.shape[0] else j

            # Get the min and max values suroudning that pixel
            min_pixel = np.min(img[y:h, x:l])
            max_pixel = np.max(img[y:h, x:l])
            
            # Apply the formula
            minmax_img[i, j] = (img[i, j] - min_pixel) / (max_pixel - min_pixel) * 255

    # Save the image
    cv.imwrite("editedImages/local_minmax.jpg", minmax_img)
