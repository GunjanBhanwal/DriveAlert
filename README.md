# Drowsiness Detection and Sleep Prevention System

This project detects drowsiness in real-time using a webcam and triggers an alarm to prevent accidents.

## Features
- Detects drowsiness based on eye blink patterns.
- Identifies yawning based on mouth movements.
- Plays an alarm and sends an email alert for prolonged drowsiness.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Download the model:
    Download shape_predictor_68_face_landmarks.dat from dlib.
    Extract it and place it in the data/ folder.

4. Run the application:

    ```bash
    python src/main.py
