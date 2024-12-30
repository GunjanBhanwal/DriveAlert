import dlib
import cv2
import os

# Use a relative path to the shape_predictor_68_face_landmarks.dat file
shape_predictor_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'shape_predictor_68_face_landmarks.dat')

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor_path)

def detect_faces(gray_frame):
    return detector(gray_frame)

def get_landmarks(gray_frame, face):
    return predictor(gray_frame, face)
