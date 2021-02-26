import cv2 as cv

img = cv.imread("testImages/groundTruths/eg1_lowcntrst.jpg", 0)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(9, 9))
cl1 = clahe.apply(img)

cv.imshow("cl1.png", cl1)
cv.waitKey(0)