from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication
)
from PIL import Image


from register_student import RegisterStudent

import numpy as np
import pickle
import cv2
import os


class StartWindow(QMainWindow):
    def __init__(self, camera=None):
        super().__init__()
        self.camera = camera

        self.central_widget = QWidget()

        self.button_register_student = QPushButton("Register Student", self.central_widget)
        self.button_train_data = QPushButton("Train Student Data", self.central_widget)
        self.button_recognise_student = QPushButton("Recognise Student", self.central_widget)
        self.button_mark_attendence = QPushButton("Mark Attendence", self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.button_register_student)
        self.layout.addWidget(self.button_train_data)
        self.layout.addWidget(self.button_recognise_student)
        self.layout.addWidget(self.button_mark_attendence)
        self.setCentralWidget(self.central_widget)

        self.button_register_student.clicked.connect(self.register_student)
        # self.button_train_data.clicked.connect(self.train_data)
        # self.button_recognise_student.clicked.connect(self.recognise_student)

    def take_photo_sample(self, student_name):
        self.camera.initialize()
        self.camera.detect_face(student_name)
        
    def register_student(self):
        self.hide()
        self.SW = RegisterStudent(self)
        self.SW.show()
        
    def recognise_student(self):
        print("Student is about to be recognise")
        self.camera.initialize()
        self.camera.recognise_student()
        
    def train_data(self):
        current_id = 0
        label_ids = {}
        y_labels = []
        x_train = []
        
        face_cascade = cv2.CascadeClassifier('./cascasdes/data/haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        
        print("Data is training")
        for root, dirs, files in os.walk("images"):
           for file in files:
               if(file.endswith("png") or file.endswith("jpg")):
                   path = os.path.join(root, file)
                   label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()

                   if not label in label_ids:
                       label_ids[label] = current_id 
                       current_id += 1
                    
                   id_ = label_ids[label]
                   
                   pil_image = Image.open(path).convert("L") # COnverting to gray scale
                   size = (550, 550)
                   final_image = pil_image.resize(size, Image.ANTIALIAS)
                   image_array = np.array(pil_image,"uint8")
                   faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors = 5)

                   for (x,y,w,h) in faces:
                       roi = image_array[y:y+h, x:x+w]
                       x_train.append(roi)
                       y_labels.append(id_)
                    #    print (x, y, w ,h)
                    #    print ("X train data is",x_train)
                    #    print ("Y labels data is",y_labels)
            
        # print ("Labels are ",y_labels)
        # print ("Train Images are ",x_train)

        with open("labels.pickle","wb") as f:
            pickle.dump(label_ids, f)

        recognizer.train(x_train,np.array(y_labels))
        recognizer.save("trainer-data.yml")
        print("Data is trained")


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exit(app.exec_())
