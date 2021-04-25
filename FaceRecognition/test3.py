import cv2
import numpy as np
import face_recognition
import os

path = 'FaceRecognition/ImagesAttendance'
images=[]
classNames=[]
myList= os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown= findEncodings(images)
print('encodeing complete')

cap = cv2.VideoCapture('FaceRecognition/ImagesBasic/video2.mp4')
while True: 
    # img=cv2.imread('FaceRecognition/ImagesBasic/wc2.jpg')
    success , img = cap.read()
    # img = cv2.resize(img,(0,0),None,0.25,0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if face_recognition.face_locations(img):

        facesCurFrame = face_recognition.face_locations(img)[0]
        # encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)
        y1,x2,y2,x1 = facesCurFrame
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img,(facesCurFrame[3],facesCurFrame[0]),(facesCurFrame[1],facesCurFrame[2]),(255,0,255),2)
        # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        # cv2.putText(img,'duc',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)


# while True:
#     success, img = cap.read()
#     #img = captureScreen()
#     img=cv2.imread('FaceRecognition/ImagesAttendance/Elon Musk.jpg')
#     img = cv2.resize(img,(0,0),None,0.25,0.25)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
#     facesCurFrame = face_recognition.face_locations(img)
#     encodesCurFrame = face_recognition.face_encodings(img,facesCurFrame)
#     y1,x2,y2,x1 = facesCurFrame[0]
#     y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
#     cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#     cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#     cv2.putText(img,'duc',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

#     # for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
#     #     matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
#     #     faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
#     #     #print(faceDis)
#     #     matchIndex = np.argmin(faceDis)
    
#     #     # if matches[matchIndex]:
#     #     if True:
#     #         # name = classNames[matchIndex].upper()
#     #         name = 'duc'
#     #         #print(name)
#     #         y1,x2,y2,x1 = faceLoc
#     #         y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
#     #         cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#     #         cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#     #         cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        
#     cv2.imshow('Webcam',img)
#     cv2.waitKey(1)

