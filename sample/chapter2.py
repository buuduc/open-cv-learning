import cv2
import numpy as np 
img = cv2.imread("Resources/wall.jpg")
imgResize=cv2.resize(img,(300,200))
imgCropped = img[0:200,200:500]
kernel =np.ones((5,5),np.uint8)
print(img.shape)
cv2.imshow(" image",img)
cv2.imshow("imgResize image",imgResize)
cv2.imshow("cropped image",imgCropped)
cv2.waitKey(0)