The Face Recognition Attendance System is a Python application that automates attendance tracking through face recognition technology.
Built using OpenCV, Tkinter, and MySQL, this system allows organizations and institutions to efficiently manage attendance records.
The project uses Local Binary Patterns Histograms (LBPH) for face detection and recognition, ensuring accurate identification.

Features
Face Recognition: Utilizes LBPH for efficient face detection and recognition.
Student Management: Includes a student management module to add, update, and delete student information.
Attendance Management: Automatically marks attendance by detecting and recognizing faces.
Database Integration: Stores student and attendance data in MySQL for easy access and management.
User-Friendly Interface: Built with Tkinter, providing a clear, navigable interface for administrators.

Installation
Prerequisites
Python 3.x
OpenCV: For image processing and face recognition.
Tkinter: For GUI development.
MySQL: To store student and attendance records.
Other Libraries: Install the required libraries with the following command:
pip install -r requirements.txt

Setting Up MySQL Database
Install MySQL and create a database (e.g., attendance_system).
Import the provided SQL script (if available) or create tables for student and attendance records.
Update database connection credentials in the code.

Usage
Add Students: Use the Student Details module to add new students, including taking face samples for recognition.
Train Model: Once face samples are collected, use the Train Data module to train the LBPH model.
Mark Attendance: Open the Attendance module, and the system will automatically detect faces and mark attendance in the database.

Structure
FACE RECOGNITION ATTENDANCE SYSTEM
│
├── __pycache__/                 # Cache files for Python
├── data/                        # Contains the captured images of students used for training the face recognition model.
├── Images/                      # Contains the images that used in interface designing
├── Attendance.csv               # CSV file for attendance records
├── attendance.py                # Module for managing attendance functions
├── classifier.xml               # Pre-trained Haar Cascade XML for face detection
├── developer.py                 # Developer information or configurations
├── face_recognition.py          # Face detection and recognition logic
├── haarcascade_frontalface.xml  # Haar Cascade model for face detection
├── help.py                      # Help module for user guidance
├── main.py                      # Main file to run the application
├── model.h5                     # Saved model file for face recognition
├── student.py                   # Student information management module
├── tempCodeRunnerFile.py        # Temporary file created by VS Code
└── train.py                     # Script for training the face recognition model

data/: Contains the captured images of students used for training the face recognition model.
Images/: Contains the images that used in interface designing
Attendance.csv: CSV file for recording attendance data.
attendance.py: Manages attendance records, including functions to mark and retrieve attendance.
classifier.xml: Pre-trained Haar Cascade XML file for face detection.
developer.py: Module that may include developer information or system configurations.
face_recognition.py: Main script for detecting and recognizing faces using LBPH.
haarcascade_frontalface.xml: Haar Cascade model for face detection.
help.py: Provides help or guidance features within the application.
main.py: Entry point for the application, launching the main interface.
model.h5: Model file (likely saved from training) for face recognition.
student.py: Manages student data, including adding, updating, and deleting student information.
tempCodeRunnerFile.py: Temporary file used by the code editor (VS Code) for running snippets.
train.py: Contains code to train the face recognition model with new student images

How to Run the Project
Install Dependencies:
Make sure you have Python and the required libraries installed.
Install necessary packages by running:
pip install opencv-python opencv-python-headless numpy pillow mysql-connector-python

Set Up Database:
Ensure MySQL is installed and running on your machine.
Create a database and configure the database connection in your code (usually in attendance.py or student.py).
Import any required database tables or run the necessary SQL scripts to initialize your tables (e.g., for student data and attendance records).

Run the Application:
Open a terminal or command prompt.
Run the main.py file by executing:
python main.py

Interface Overview:
Running main.py will launch the main interface of the Face Recognition Attendance System.
The main screen has options for:
Student Details: Manage student information.
Face Detector: Capture and recognize faces.
Attendance: Mark attendance based on recognized faces.
Train Data: Train the model with newly added student images.
Help: Get guidance on how to use the system.
Exit: Close the application.

Using the System:
Add Student: Go to the "Student Details" section to add or update student information. This includes taking photo samples for training.
Train Model: After adding student photos, go to "Train Data" to update the model with new faces.
Mark Attendance: Use the "Attendance" option to start face recognition and mark attendance automatically.
Check Records: Attendance is saved in Attendance.csv and can be reviewed or managed
