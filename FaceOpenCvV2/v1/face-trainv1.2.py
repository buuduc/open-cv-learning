import os
import cv2
import face_recognition
# from PIL import Image
import numpy as np
import pickle
import imutils
BASE_DIR = os.path.dirname(os.path.abspath(__file__ )) 
# img_dir= os.path.join(BASE_DIR,"images")
img_dir='FaceOpenCvV2/images'
current_id =0 
label_ids={}
y_labels=[]
x_train=[]
stt=0






# path='FaceOpenCv/images/atien/20210426_112422.jpg'
# pil_image = cv2.imread(path)
# pil_image=imutils.resize(pil_image,width=500)
# pil_image=cv2.cvtColor(pil_image,cv2.COLOR_BGR2GRAY)
# # pil_image=Image.open(path).convert('L')
# # final_image=pil_image.resize((550,550))

# # image_array=np.array(final_image,'uint8')
# faces = face_cascade.detectMultiScale(pil_image,scaleFactor=1.2,minNeighbors=7)

# for (x,y,w,h) in faces:
#     print(x,y,w,h)
#     roi = pil_image[y:y+h,x:x+w]
#     cv2.rectangle(pil_image, (x, y), (x+w, y +h), (0, 255,0), 2)

# cv2.imshow('nhieu mat',pil_image)
# cv2.waitKey(0)



for root,dirs,files in os.walk(img_dir):
    faceEncodeArray=[]
    faceNameArray=[]
    label=os.path.basename(root).replace(' ','-').lower()
    label = os.path.splitext(label)[0]
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('JPG'):
            path = os.path.join(root,file)
            # print(label,path)
            if not  label in label_ids:
                current_id+=1
                label_ids[label]=current_id
                id_= label_ids[label]
            # print(label_ids)
            # y_labels.append(label) 
            # x_train.append(path)

            pil_image = cv2.imread(path)
            # pil_image=imutils.resize(pil_image,width=500)
            image_array=cv2.cvtColor(pil_image,cv2.COLOR_BGR2RGB)
            # image_array=cv2.resize(image_array,(0,0),None,0.5,0.5)
            facesCurFrame = face_recognition.face_locations(image_array)
            facesEncoding=face_recognition.face_encodings(image_array)
            # face 
            if facesCurFrame:
                for face,encode in zip(facesCurFrame,facesEncoding):
                    stt+=1
                    # print(faces)
                    cv2.rectangle(image_array,(face[3],face[0]),(face[1],face[2]),(255,0,255),2)
                    cv2.imwrite(f'anhtest/{label}-{stt}.jpg',image_array)
                    faceEncodeArray.append(encode)
                    faceNameArray.append(label)
                    print(f'anhtest/{label}-{stt}.jpg')



cap = cv2.VideoCapture(0)
while True: 
    # img=cv2.imread('FaceRecognition/ImagesBasic/wc2.jpg')
    success , img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(0,0),None,0.5,0.5)
    if face_recognition.face_locations(img):

        facesCurFrame = face_recognition.face_locations(img)[0]
        encodesCurFrame = face_recognition.face_encodings(img)[0]
        y1,x2,y2,x1 = facesCurFrame
        cv2.rectangle(img,(facesCurFrame[3],facesCurFrame[0]),(facesCurFrame[1],facesCurFrame[2]),(255,0,255),2)
        matches = face_recognition.compare_faces(faceEncodeArray,encodesCurFrame)
        faceDis = face_recognition.face_distance(faceEncodeArray,encodesCurFrame)
        print(faceDis,matches)
        index=np.argmin(faceDis)
        print(faceNameArray[index])


        # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        # cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        # cv2.putText(img,'duc',(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    resizeCamera=cv2.resize(img,(720,480))
    cv2.imshow('Webcam',resizeCamera)
    cv2.waitKey(1)


            
           

            # for (x,y,w,h) in faces:
            #     roi = image_array[y:y+h,x:x+w]
            #     # print(x_train)
            #     print(label,stt)
            #     print(w,h)
            #     print(y_labels)
            #     x_train.append(roi)
            #     y_labels.append(id_)
            #     cv2.rectangle(pil_image, (x, y), (x+w, y +h), (0, 255,0), 2)

            # stt+=1
            # # cv2.imshow(f'{stt}: {label}',image_array)
            # cv2.imwrite(f'anhtest/{label}-{stt}.jpg',pil_image)
                

with open('labels.pickle','wb') as f:
    pickle.dump(label_ids,f )


# recognizer.train(x_train,np.array(y_labels))
# recognizer.save("trainner.yml")
# cv2.waitKey(0)