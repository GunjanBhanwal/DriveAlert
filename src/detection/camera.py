import cv2

def initialize_camera():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise Exception("Error: Camera not found.")
    
    return cap
