import cv2
import numpy as np 
imp
img = cv2.imread("Resources/lambo.png")
img=cv2.resize(img,(300,200))
kernel =np.ones((5,5),np.uint8)
print(img.shape)
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0) 
imgCanny=cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgEroded )
cv2.imshow("Eroded image",imgEroded)
cv2.imshow('gg',im)
cv2.waitKey(0)