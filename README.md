#SnapClass – AI-Powered Attendance Management System:-

1.SnapClass is an AI-powered attendance management system designed to make classroom attendance faster, easier, and more reliable.

2.Traditional attendance methods are time-consuming for teachers and can lead to manual errors. SnapClass automates the attendance
  process using face recognition while also providing a complete platform for managing students, subjects, classes, and attendance records.
  
3.The system provides separate workflows for teachers and students, making classroom attendance management simple and organized.

## 🎯Objective:-

1.The main objective of SnapClass is to reduce the time and effort required for manual attendance.

2.The system allows teachers to manage subjects, share classes with students, take attendance using face recognition, and view attendance 
records. Students can register using their face, log in through face recognition, join subjects using class codes or shared links, 
and track their attendance.

## ✨Key Features

### 👨‍🏫Teacher Features:-

- Teacher registration and login
- Create and manage subjects
- Manage different classes and sections
- Share subjects using class codes
- Generate QR codes for class joining
- Share class joining links
- Take attendance using face recognition
- View attendance records
- Track student attendance for different subjects

### 👩‍🎓Student Features:-

- Student registration using face recognition
- Face-based student login
- Student dashboard
- View enrolled subjects
- View attendance statistics
- Join subjects using class codes
- Join classes through shared links
- Enroll and unenroll from subjects
- Optional voice enrollment


## 🤖Face Recognition System:-

Face recognition is the core AI feature of SnapClass.

The recognition pipeline works in the following steps:

1. The system captures an image using the camera.
2. Dlib detects the face in the image.
3. Facial landmarks are extracted from the detected face.
4. The face recognition model converts the facial features into a 128-dimensional face embedding.
5. The generated embedding is compared with the face embeddings stored in the database.
6. Euclidean distance is used to measure the similarity between the new face and stored embeddings.
7. If the distance is within the configured recognition threshold, the student is recognized.
8. If the face is not recognized, the system provides an option to register as a new student.

-This approach allows the same registered student to log in using their face without manually entering credentials every time.


## 🔄Student Workflow:-
 
      Student
         ↓
      Face Login
         ↓
      Face Detection
         ↓
      Face Recognition
         ↓
      Recognized?
         ├── Yes → Student Dashboard
         │            ↓
         │       View Subjects
         │            ↓
         │       View Attendance
         │
         └── No → New Student Registration
                    ↓
                Create Profile
                    ↓
                Store Face Embedding
      
## 🔄Teacher Workflow:-

      Teacher
         ↓
      Register / Login
         ↓
      Teacher Dashboard
         ↓
      Create / Manage Subject
         ↓
      Share Class Code / Link / QR
         ↓
      Students Join the Subject
         ↓
      Take Attendance
         ↓
      View Attendance Records

---

## 📱 QR-Based Class Joining:-

1.SnapClass provides a simple way for teachers to share their classes with students.
2.For each subject, the teacher can generate a QR code containing the class joining link along with the subject code.
3.Students can use the shared link or scan the QR code to access and join the respective subject.
4.This makes class sharing easier and reduces the need for teachers to manually add students to every class.


## 🗄️ Database:-

1.SnapClass uses a database to store and manage the application's core data.
2.The database manages information related to:

- Students
- Teachers
- Subjects
- Student-subject relationships
- Attendance records
- Face embeddings
- Optional voice embeddings

These relationships allow attendance to be maintained separately for different students, subjects, and classes.


## 🛠️Tech Stack:-

1.Programming Language
- Python

2.Application Framework
- Streamlit

3.AI / Machine Learning
- Dlib
- Face Recognition Model
- NumPy
- Scikit-learn

4.Database
- Supabase

5.Additional Technologies
- Segno – QR code generation
- Pillow – Image processing
- Librosa – Audio processing
- Resemblyzer – Voice embedding support
- Bcrypt – Password hashing


## ⚙️How It Works:-

### 1. Student Registration

-A new student captures their face using the camera and provides their name.
-The system generates a face embedding from the captured image and stores it with the student's profile in the database.

### 2. Student Login

-When an existing student captures their face, the system generates a new face embedding and compares it with the stored embeddings.
-If a matching embedding is found within the configured recognition threshold, the student is recognized and logged into their 
dashboard.

### 3. Subject Management

-Teachers can create and manage subjects, classes, and sections from the teacher dashboard.

### 4. Class Sharing

-Teachers can share a subject using a class code, joining link, or QR code.

### 5. Attendance

-The teacher selects a subject and uses face recognition to identify registered students and record their attendance.

### 6. Attendance Records

-Attendance data is stored in the database and can be viewed by teachers through the Attendance Records section.
-Students can also view their attendance statistics from their dashboard.


## 🚧Challenges and Solutions:-

### 1. Avoiding Incorrect Face Matches

-One of the main challenges was making face recognition reliable while avoiding incorrect student matches.
-To address this, SnapClass compares face embeddings using Euclidean distance and applies a configurable recognition threshold.
 A student is recognized only when the calculated distance meets the defined condition.

### 2. Handling Different Face Detection Cases

The system handles different scenarios such as:

- No face detected
- Multiple faces detected
- Face not recognized
- Recognized student

This helps prevent invalid or incorrect attendance entries.

### 3. Updating Recognition Data

-When a new student registers, their face embedding is stored in the database and the recognition system is updated so that the student can be recognized during future logins.

### 4. Managing Multiple Subjects

-Attendance needs to be maintained separately for different subjects and classes.
-SnapClass handles this through relationships between students, subjects, and attendance records in the database.


## 🚀Future Improvements:-

Some possible future improvements include:

- Improved face recognition under different lighting conditions
- Liveness detection and anti-spoofing
- Advanced attendance analytics
- Attendance report export
- More advanced voice-based verification
- Improved mobile experience


## 🎥 Demo:-

**Live Demo:**  
https://snapclass-main0948.streamlit.app/

The live application demonstrates the student and teacher workflows, including face-based login, subject management, class sharing, QR generation, attendance, and attendance records.

## 👩‍💻 Author:-

**Ananya Sah**


## ❤️About the Project:-

-SnapClass was built to explore how AI-based face recognition can be integrated into a complete real-world application to solve a
practical problem in classroom attendance management.

-The project combines AI, database management, web application development, and user-focused workflows into a single attendance management 
system.
