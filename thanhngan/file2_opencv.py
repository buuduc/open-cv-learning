import cv2
#reading Image
image = cv2.imread('./Resources/wall.png')
#show you image ,provide window name first
cv2.imshow('image window',image)
#add wait key. window waits till user press any key
cv2.waitKey(0)
#and finally destroy/Closing all open windows
cv2.destroyAllWindows()