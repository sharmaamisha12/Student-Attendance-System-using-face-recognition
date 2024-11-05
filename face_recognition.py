from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x864+0+0")  # Adjust window size
        self.root.title("Face Recognition System")
        
        # Initialize a set to track attendance for the session
        self.marked_attendance_ids = set()

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(relx=0, rely=0, relwidth=1, height=45)

        # Load images
        img_top = Image.open(r"Images\k.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"Images\upscaled_img.jpeg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=375, y=620, width=200, height=40)

    # ========Attendance========
    def mark_attendance(self, student_id, roll_number, name, department):
        # Get the current date and time
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")

        # Check if the student ID is already marked for attendance in this session
        if student_id in self.marked_attendance_ids:
            return  # If already marked, do not add again

        # Add to marked attendance set
        self.marked_attendance_ids.add(student_id)

        # Append the attendance record to the CSV file
        with open("Attendance.csv", "a", newline="") as f:
            f.write(f"{student_id},{roll_number},{name},{department},{current_time},{current_date},Present\n")

    # ======face recognition=======  
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="amisha", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id = %s", (str(id),))
                student = my_cursor.fetchone()

                if student:
                    n, r, d, i = student
                else:
                    n, r, d, i = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    self.mark_attendance(i, r, n, d)  # Mark attendance here
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
        except Exception as e:
            messagebox.showerror("Error", f"OpenCV LBPHFaceRecognizer Error: {str(e)}")
            return

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to break the loop
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
