import numpy as np

def compute(ptA, ptB):
    """
    Compute the Euclidean distance between two points.
    :param ptA: First point (x1, y1)
    :param ptB: Second point (x2, y2)
    :return: Euclidean distance
    """
    return np.linalg.norm(np.array(ptA) - np.array(ptB))

def is_blinking(landmarks):
    """
    Detect if a person is blinking based on the Eye Aspect Ratio (EAR).
    :param landmarks: Dlib landmarks object
    :return: Tuple of (sleep_status, drowsy_status)
    """
    # Extract coordinates for left and right eyes
    left_eye_points = [landmarks.part(i) for i in range(36, 42)]
    right_eye_points = [landmarks.part(i) for i in range(42, 48)]

    def eye_aspect_ratio(eye_points):
        # Convert to (x, y) tuples
        eye_points = [(p.x, p.y) for p in eye_points]
        # Vertical distances
        vertical1 = compute(eye_points[1], eye_points[5])
        vertical2 = compute(eye_points[2], eye_points[4])
        # Horizontal distance
        horizontal = compute(eye_points[0], eye_points[3])
        # Eye Aspect Ratio (EAR)
        return (vertical1 + vertical2) / (2.0 * horizontal)

    left_ear = eye_aspect_ratio(left_eye_points)
    right_ear = eye_aspect_ratio(right_eye_points)

    # Thresholds for EAR
    sleeping_threshold = 0.2  # A very low EAR indicates sleeping
    drowsy_threshold = 0.25   # A lower EAR threshold for drowsiness
    active_threshold = 0.3    # A higher EAR threshold indicating alertness

    # Sleeping condition: EAR below sleeping threshold
    if left_ear < sleeping_threshold or right_ear < sleeping_threshold:
        return 0, 0  # Sleeping: Both eyes closed (or nearly closed)

    # Drowsy condition: EAR is low but above sleeping threshold
    elif left_ear < drowsy_threshold or right_ear < drowsy_threshold:
        return 1, 1  # Drowsy: Prolonged blinking or eyes partially closed

    # Active condition: Both eyes are open, EAR is above drowsy threshold
    else:
        return 1, 0  # Active: Eyes open and no signs of drowsiness
