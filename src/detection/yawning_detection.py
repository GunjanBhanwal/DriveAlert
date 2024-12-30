import numpy as np

def compute(ptA, ptB):
    ptA = (ptA.x, ptA.y)
    ptB = (ptB.x, ptB.y)
    return np.linalg.norm(np.array(ptA) - np.array(ptB))

def mouth_aspect_ratio(mouth_points):
    vertical1 = compute(mouth_points[2], mouth_points[10])
    vertical2 = compute(mouth_points[4], mouth_points[8])
    horizontal = compute(mouth_points[0], mouth_points[6])
    return (vertical1 + vertical2) / (2.0 * horizontal)

def is_yawning(landmarks):
    mouth_points = [landmarks.part(i) for i in range(48, 68)]
    mar = mouth_aspect_ratio(mouth_points)
    return mar > 0.6