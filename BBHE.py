import cv2
import numpy as np


def bbhe(img):
    """
    :param img: From the implementation point of view, it is still a grayscale image
         :return: return the modified image
    """
    # xm = np.exp(9)
    xmin = np.min(img)
    xmax = np.max(img)
    img_result = np.zeros_like(img)
    # Average gray value
    xm = np.mean(img)

    sl = np.zeros((256, 1))  # The image is divided into two parts l and u
    su = np.zeros((256, 1))
    pl = np.zeros((256, 1))
    pu = np.zeros((256, 1))
    hist_cl = np.zeros((256, 1))
    hist_cu = np.zeros((256, 1))
    nl = 0
    nu = 0

    # Count the pixels in the image and classify them
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] < xm:
                sl[img[i, j] - 1] += 1
                nl += 1
            else:
                su[img[i, j] - 1] += 1
                nu += 1
    pl = sl / nl
    pu = su / nu

    hist_cl = np.cumsum(pl)
    hist_cu = np.cumsum(pu)

    hist_cl = xmin + hist_cl * (xm - xmin)
    hist_cu = xm + 1 + hist_cu * (xmax - xm - 1)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] <= xm:
                temp = img[i, j]
                img_result[i, j] = hist_cl[temp - 1]
            else:
                temp = img[i, j]
                img_result[i, j] = hist_cu[temp - 1]

    return img_result


def hsv_bbhe(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = bbhe(img_gray).astype(np.uint8)
    result = cv2.merge((h, s, img_gray))
    result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    return result
