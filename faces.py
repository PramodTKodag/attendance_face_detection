import numpy as np
import cv2
import time
import pickle

face_cascade = cv2.CascadeClassifier('./cascasdes/data/haarcascade_frontalface_default.xml')
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read("trainer.yml")

# labels = {}
# with open("labels.pickle","rb") as f:
#     org_labels = pickle.load(f)
#     labels = {v:k for k,v in org_labels.items()}

cap = cv2.VideoCapture(1)

# print("Labels are ",labels)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 5)

    for (x, y , w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # recognize deep learning model predict
        # id_, conf = recognizer.predict(roi_gray)
        # # print ("COnfidence is ",conf)
        # if conf >= 45 and conf <= 100:
        #     # print(id_) 
        #     print(labels[id_])
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     name = labels[id_]
        #     color = (255,255,255)
        #     stroke = 2
        #     cv2.putText(frame, name, (x,y), font, 1, color, stroke,cv2.LINE_AA )
            
            # pass

        # img_item = "my-image.png"
        # cv2.imwrite(img_item,roi_color)

        color = (255,0,0) #BGR 0-255
        stroke = 1
        end_coordinate_x = x + w
        end_coordinate_y = y + h
        cv2.rectangle(frame, (x,y), (end_coordinate_x,end_coordinate_y), color, stroke ) 


    
    
    cv2.imshow('frame',frame)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()