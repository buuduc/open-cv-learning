import cv2
import numpy as np
img = cv2.imread('Resources/lena.png')
imgHor= np.hstack((img,img))

cv2.imshow("ggg",imgHor)
cv2.waitKey(0)