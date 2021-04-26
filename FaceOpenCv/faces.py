import numpy as np
import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('FaceOpenCv/data/haarcascade_frontalface_alt2.xml')
while(True):
    # capture frame by frame 
    ret,frame = cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for x,y,w,h in faces:
        print(x,y,w,h)
        roi_gray= gray[y:y+h, x:x+w]
        img_item="my-image.png"
        cv2.imwrite(img_item,roi_gray)

        color =(255,0,0)
        stroke =2 
        end_cord_x = x + w 
        end_cord_y= y + h 
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
    
    
    
    cv2.imshow('frame' , frame) 
    if cv2.waitKey(20) & 0xFF == ord('q'): 
        break



# Display the resulting frame 
cap.release()
cv2.destroyAllWindows()
     

    