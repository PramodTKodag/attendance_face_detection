import os

import numpy as np
import cv2
import time
import pickle

directory_name = "Test Data"
face_cascade = cv2.CascadeClassifier('./cascasdes/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
with open("labels.pickle","rb") as f:
    org_labels = pickle.load(f)
    labels = {v:k for k,v in org_labels.items()}

def load_test_image(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

if __name__ == "__main__":
    for file in load_test_image(directory_name):
        print("File is ",file)
        img = cv2.imread(directory_name+"/"+file, 1)
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5)

        for (x, y , w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # recognize deep learning model predict
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45 and conf <= 100:
            
                print("Face detected")
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (0 ,0,0)
                stroke = 2
                cv2.putText(img, name, (x,y), font, 1, color, stroke,cv2.LINE_AA )               

            color = (255,0,0) #BGR 0-255
            stroke = 1
            end_coordinate_x = x + w
            end_coordinate_y = y + h
            # print("end corordinat x",end_coordinate_x)
            # print("end corordinat y",end_coordinate_y)

            cv2.rectangle(img, (x,y), (end_coordinate_x,end_coordinate_y), color, stroke ) 

        cv2.imshow('Image', img)
        cv2.waitKey(0)
    
    cv2.destroyAllWindows()