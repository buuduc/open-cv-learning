import cv2
import pytesseract

img_cv = cv2.imread('bienso.jpg')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
cv2.imshow('gg',img_cv)
print(pytesseract.image_to_string(img_cv))
cv2.waitKey(0)