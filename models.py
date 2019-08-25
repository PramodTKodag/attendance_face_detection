import cv2
import pickle
import os

import xlwt

from xlsxwriter.workbook import Workbook

import openpyxl
from openpyxl import load_workbook

from datetime import datetime
from pytz import timezone

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QMessageBox

import PyQt5
from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])



import mysql.connector
connn = mysql.connector.connect(user='root',password='root',host='localhost',port='3306',database='attendence_system')

class Camera:

    def __init__(self, cam_num):
        self.cap = None
        self.cam_num = cam_num
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.face_cascade = cv2.CascadeClassifier('./cascasdes/data/haarcascade_frontalface_default.xml')
        self.folder_name = "images"

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def detect_face(self, student_name):
        counter = 0
        while(True):
            frame = self.get_frame()
            gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_face, scaleFactor=1.5, minNeighbors = 5)

            path = "{folder_name}/{student_name}".format(
                    folder_name = self.folder_name,
                    student_name = student_name,
            )

            if not os.path.exists(path):
                    os.mkdir(path)

            for (x, y, w, h) in faces:
                counter += 1

                image_path = path + "/{counter}.jpg".format(
                    counter = counter
                )

                print("IMage path is ", image_path)
                cv2.imwrite(image_path, gray_face)

                print("Face is ", x, y, w , h)
                color = (255,0,0)
                stroke = 1
                end_coordinate_x = x + w
                end_coordinate_y = y + h
                cv2.rectangle(frame, (x,y), (end_coordinate_x,end_coordinate_y), color, stroke )

            cv2.imshow('Capture Student Photo', frame)

            if counter == 200:
                self.close_camera("Capture Student Photo")
                break

            if cv2.waitKey(20) & 0xFF == ord('q'):
                self.close_camera("Capture Student Photo")
                break

            if cv2.getWindowProperty('Capture Student Photo',cv2.WND_PROP_VISIBLE) < 1:
                self.close_camera("Capture Student Photo")
                break

    def recognise_student(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer-data.yml")
        conf = 0
        labels = {}
        with open("labels.pickle","rb") as f:
            org_labels = pickle.load(f)
            labels = {v:k for k,v in org_labels.items()}
        while(True):
            frame = self.get_frame()
            gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray_face, scaleFactor=1.5, minNeighbors = 5)

            for (x, y, w, h) in faces:
                roi_gray = gray_face[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                id_, conf = recognizer.predict(roi_gray)
                print ("COnfidence is ",conf)
                if conf >= 45 and conf <= 100:
                    # print(id_)
                    print("Found a Person : "+labels[id_])
                    try:
                        format = "%Y-%m-%d %H:%M:%S"
                        # Current time in UTC
                        now_utc = datetime.now(timezone('UTC'))
                        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
                        add_time = now_asia.strftime(format)

                        format = "%Y-%m-%d"
                        # Current time in UTC
                        now_utc = datetime.now(timezone('UTC'))
                        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
                        add_time2 = now_asia.strftime(format)

                        cur = connn.cursor()

                        cur.execute("SELECT * from attendance where Name='%s' and date_today='%s'"%(labels[id_], add_time2))
                        res12 = cur.fetchall()
                        
                        if(len(res12)==0):
                            cur.execute("INSERT into attendance (Name, date_today) values('%s', '%s')"%(labels[id_], add_time))
                            

                        else:
                            print("attendance already punched")

                        book = xlwt.Workbook("Attendance-sheet.xls")
                        sheet1 = book.add_sheet("Sheet 1")


                        date_format = xlwt.XFStyle()
                        date_format.num_format_str = 'dd/mm/yyyy HH:MM:SS'

                        cur.execute("select * from attendance")
                        results = cur.fetchall()
                        sheet1.write(0, 0, "ID")
                        sheet1.write(0, 1, "NAME")
                        sheet1.write(0, 2, "Date and Time")
                        xax = 1
                        for row in results:

                            sheet1.write(xax, 0, row[0])
                            sheet1.write(xax, 1, row[1])
                            sheet1.write(xax, 2, row[2], date_format)

                            xax+=1
                            book.save("Attendance-sheet.xls")
                    except Exception as e:
                        print("Data insertation error : "+str(e))
                    cur.close()
                    connn.commit()
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = labels[id_]
                    color = (255,255,255)
                    stroke = 2
                    cv2.putText(frame, name, (x,y), font, 1, color, stroke,cv2.LINE_AA )

                color = (255,0,0)
                stroke = 1
                end_coordinate_x = x + w
                end_coordinate_y = y + h
                cv2.rectangle(frame, (x,y), (end_coordinate_x,end_coordinate_y), color, stroke )

            cv2.imshow('Recognise Student', frame)

            # if conf >= 45 and conf <= 100:
            #     self.close_camera("Recognise Student")
            #     break

            if cv2.waitKey(20) & 0xFF == ord('q'):
                self.close_camera("Recognise Student")
                break

            if cv2.getWindowProperty('Recognise Student',cv2.WND_PROP_VISIBLE) < 1:
                self.close_camera("Recognise Student")
                break


    def set_brightness(self, value):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)

    def close_camera(self, window_name=None):
        if window_name:
            cv2.destroyWindow(window_name)
        else:
            cv2.destroyAllWindows()
        self.cap.release()

    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)


if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    cam.set_brightness(1)
    print(cam.get_brightness())
    cam.set_brightness(0.5)
    print(cam.get_brightness())
    frame = cam.get_frame()
    print(frame)
    # cam.close_camera()
