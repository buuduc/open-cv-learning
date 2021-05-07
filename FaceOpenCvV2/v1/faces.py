import numpy as np
import cv2
import pickle
from datetime import datetime, timedelta
from csv import writer

peopleCheckin ={}
# def markAttendance(name):
#     with open('Attendance.csv','r+') as f:
#         myDataList=f.readlines()
        
#         nameList=[]
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#             print(nameList)
#             if name not in nameList:
#                 now = datetime.now()
#                 dtString= now.strftime('%H:%M:%S  %D')
#                 f.writelines(f'\n{name},{dtString}')


def markAttendance(name):

        # Open file in append mode
    with open('Attendance.csv', 'a+', newline='') as write_obj:
        now = datetime.now()
        dtString= now.strftime('%H:%M:%S  %D')
        
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([name,dtString])

    # with open('Attendance.csv','w') as f:
    #     now = datetime.now()
    #     dtString= now.strftime('%H:%M:%S  %D')
    #     f.writelines(f'\n {name},{dtString}')
    #     print(f'\n {name},{dtString}')
    
def checkAttendance(name):
    if name not in peopleCheckin:
        peopleCheckin[name]={'time': datetime.now()-timedelta(seconds=50),'count': 1,'checkin': False}
    if datetime.now() - peopleCheckin[name]['time'] > timedelta(seconds=5):
        if peopleCheckin[name]['count']>10:
            peopleCheckin[name]['count']=0
            peopleCheckin[name]['checkin']=True
            peopleCheckin[name]['time']=datetime.now()
            markAttendance(name)
            
        else:
            peopleCheckin[name]['count']+=1
    # print(peopleCheckin[name])

def initAttendance():
    with open('Attendance.csv','w') as f:
        f.writelines('Name, Date \n')
def deleteFrameCheck():
    for key in peopleCheckin:
                peopleCheckin[key]['count']=0


def recForFace(img,name,x,y,w,h):
    stroke =2 
    end_cord_x = x + w 
    end_cord_y= y + h 
    if (name == 'unknown'):
        color =(255,0,0)
        check='unknown human'
    elif peopleCheckin[name]['checkin']:
        color =(0,255,0)
        check ='checked'
    else:
        color =(0,0,255)
        check ='uncheck'
    cv2.rectangle(frame,(x,y),(end_cord_x,y-20),color,cv2.FILLED) #o unknown tren cung
    cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
    cv2.rectangle(frame,(x,end_cord_y-35),(end_cord_x,end_cord_y),color,cv2.FILLED) #o ten ben duoi
    cv2.putText(frame,name,(x+6,end_cord_y-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)# CHU XUAT HIEN BEN DUOI


    cv2.putText(frame,check,(x+6,y-2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)


initAttendance()
cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
face_cascade=cv2.CascadeClassifier('FaceOpenCv/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('FaceOpenCv/data/haarcascade_eye.xml') 
smile_cascade =cv2.CascadeClassifier('FaceOpenCv/data/haarcascade_smile.xml') 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {'person_name':1 }
with open('labels.pickle','rb') as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}

# def recrec():


# print(labels)
while(True):
    # capture frame by frame 
    ret,frame = cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4,minSize=(50,50))
    if len(faces)==0 :
        deleteFrameCheck()
    for x,y,w,h in faces:
        # print(x,y,w,h)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        roi_gray= gray[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]

# recognize? deep learned model predict keras tensorflow pytorch scikit learn 
        id_,conf =recognizer.predict(roi_gray)
        print(id_,conf)
        if conf>=30 and conf <=100:
            # print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name= labels[id_]
            color = (0,0,255)
            color2=(0,255,0)
            stroke =2
            # cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            checkAttendance(name)
            recForFace(frame,name,x,y,w,h)
        else:
            recForFace(frame,'unknown',x,y,w,h)
            


        # img_item="my-image.png"
        # cv2.imwrite(img_item,roi_gray)

        # color =(0,0,255)
        # stroke =2 
        # end_cord_x = x + w 
        # end_cord_y= y + h 
        # cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)
        # cv2.rectangle(frame,(x,end_cord_y-35),(end_cord_x,end_cord_y),(0,0,255),cv2.FILLED)
        # cv2.putText(frame,name,(x+6,end_cord_y-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


        # subitems=smile_cascade.detectMultiScale(roi_gray) 
        # for (ex,ey,ew,eh) in subitems:
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey +eh), (0, 255,0), 2)


        # eyes=eye_cascade.detectMultiScale(roi_gray) 
        # for (ex,ey,ew,eh) in eyes:
        #     print('ex')
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey +eh), (0, 255,0), 2)

    
    
    
    cv2.imshow('frame' , frame) 
    if cv2.waitKey(20) & 0xFF == ord('q'): 
        break



# Display the resulting frame 
cap.release()
cv2.destroyAllWindows()
     

    