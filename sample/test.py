import cv2
import pytesseract 
# print("package import")
# img = cv2.imread('test.jpg')
# cv2.imshow('test',img)
# cv2.waitKey(1000)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
print(cap.read())
while True:
  success, img = cap.read()
  cv2.imshow('Video',img)
  if cv2.waitKey(1) & 0xFF ==ord('q'):
      break