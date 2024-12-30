import cv2
from detection.face_detection import detect_faces, get_landmarks
from detection.blink_detection import is_blinking
from detection.yawning_detection import is_yawning
from detection.alarm import play_alarm, stop_alarm
from utils.email_utils import send_email_in_background  


sleep_counter = 0
drowsy_counter = 0
active_counter = 0
yawn_counter = 0
alarm_played_count = 0
status = ""
color = (0, 0, 0)

def main():
    global sleep_counter, drowsy_counter, active_counter, yawn_counter, alarm_played_count, status, color

    
    cap = cv2.VideoCapture(0)  

    while True:
        
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from the camera.")
            break

        
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        faces = detect_faces(gray)
        for face in faces:
            
            landmarks = get_landmarks(gray, face)

            
            left_blink, right_blink = is_blinking(landmarks)

            if left_blink == 0 and right_blink == 0:  
                sleep_counter += 1
                drowsy_counter = 0
                active_counter = 0
                if sleep_counter >= 6:
                    play_alarm()
                    status = "SLEEPING !!!"
                    color = (255, 0, 0)  
                    alarm_played_count += 1
                    if alarm_played_count >= 5:  
                        send_email_in_background()  
                        alarm_played_count = 0  
            elif left_blink == 1 and right_blink == 1:  
                sleep_counter = 0
                active_counter = 0
                drowsy_counter += 1
                if drowsy_counter >= 6:
                    status = "Drowsy..."
                    color = (0, 0, 255)  
            else:  
                status = "Active :)"
                color = (0, 255, 0)
                stop_alarm()  
                drowsy_counter = 0
                sleep_counter = 0

            
            if is_yawning(landmarks):
                yawn_counter += 1
                if yawn_counter > 5:
                    status = "Yawning and drowsy"
                    color = (0, 255, 255)  
                    sleep_counter = 0
                    drowsy_counter = 0
                    active_counter = 0
                    yawn_counter = 0
                    alarm_played_count = 0
                    play_alarm()  
                else:
                    status = "Yawning!"
                    color = (0, 255, 255)  

            
            cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        
        cv2.imshow("Driver Drowsiness Detection", frame)

        
        if cv2.waitKey(1) == 27:
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 