# isme hm face detect karenge kitna bada chota h ye sb 
# face image -> Fcae detector(dlib) -> shape predictor(landmarks) -> face embedding(128D ResNet) -> compare with database embeddings

import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students


@st.cache_resource  #ye use krke bar bar data call nhi hoga bus re run hoga qki heavy data hota h
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()


    sp=dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location())

    facerec=dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location())

    return detector,sp,facerec


def  get_face_embedding(image_np):
    detector,sp,facerec=load_dlib_models()
    faces = detector(image_np,1)

    encodings =[]
    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_descriptor(image_np,shape,1)  #128 embedding
        encodings.append(np.array(face_descriptor))
    return encodings


@st.cache_resource
def get_trained_model():
    x = [] 
    y = []

    student_db = get_all_students()

    if not student_db:
        return None
    for student in student_db:
        embeddding = student.get('face_embedding')
        if embeddding:
            x.append(np.array(embeddding))
            y.append(student.get('student_id'))


    if len(x) == 0:
        return None

    clf = SVC(kernel='linear', probability=True,class_weight='balanced')

    try:
        clf.fit(x, y)
    except ValueError:
        pass
    return {'clf': clf, 'x': x, 'y': y}


def train_classifier():
    st.cache_resource.clear()  # Clear the cache to retrain the model
    model_data = get_trained_model()
    return bool(model_data)

# def predict_attendance(class_image_np):
#     encodings = get_face_embedding(class_image_np)

#     detected_students = {}

#     model_data = get_trained_model()

#     if not model_data:
#         return detected_students,[],len(encodings)

#     clf = model_data['clf']
#     x_train=model_data['x']
#     y_train=model_data['y']

#     all_students = sorted(list(set(y_train)))

#     for encoding in encodings:
#         if len(all_students) >=2:
#             predicted_id = int(clf.predict([encoding])[0])
#         else:
#             predicted_id = int(all_students[0])  # Agar sirf ek student hai to uska ID directly assign kar do
#         student_embedding = x_train[y_train.index(predicted_id)]

#         best_match_score = np.linalg.norm(student_embedding - encoding)

#         resemblance_threshold = 0.6  # Adjust this threshold based on your requirements

#         if best_match_score < resemblance_threshold:
#             detected_students[predicted_id] = True
#     return detected_students,all_students,len(encodings)
def predict_attendance(class_image_np):
    encodings = get_face_embedding(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_students, [], len(encodings)

    x_train = model_data['x']
    y_train = model_data['y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        best_distance = float("inf")
        best_student_id = None

        for student_embedding, student_id in zip(x_train, y_train):
            distance = np.linalg.norm(
                np.array(student_embedding) - np.array(encoding)
            )

            if distance < best_distance:
                best_distance = distance
                best_student_id = student_id

        resemblance_threshold = 0.55

        if best_distance < resemblance_threshold:
            detected_students[int(best_student_id)] = True

    return detected_students, all_students, len(encodings)
