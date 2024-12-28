import cv2
import numpy as np

def calculate_eye_center(eye_points):
    x_coords = [p[0] for p in eye_points]
    y_coords = [p[1] for p in eye_points]
    return (int(np.mean(x_coords)), int(np.mean(y_coords)))

def calculate_pupil_position(eye_region, frame):
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)
    eye_points = np.array(eye_region, dtype=np.int32)
    cv2.fillPoly(mask, [eye_points], 255)

    gray_eye = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye_roi = cv2.bitwise_and(gray_eye, gray_eye, mask=mask)

    _, thresh_eye = cv2.threshold(eye_roi, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh_eye, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None

    largest_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(largest_contour)
    if M["m00"] == 0:
        return None
    return (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

def analyze_gaze(face, eye_regions, frame):
    left_eye, right_eye = eye_regions
    left_pupil = calculate_pupil_position(left_eye, frame)
    right_pupil = calculate_pupil_position(right_eye, frame)

    if not left_pupil or not right_pupil:
        return "Unknown", None, None

    avg_x = (left_pupil[0] + right_pupil[0]) / 2
    avg_y = (left_pupil[1] + right_pupil[1]) / 2
    gaze_vector = (avg_x, avg_y)

    if avg_x < -20:
        direction = "Left"
    elif avg_x > 20:
        direction = "Right"
    elif avg_y < -20:
        direction = "Up"
    else:
        direction = "Down"

    return direction, (left_pupil, right_pupil), gaze_vector

def log_gaze_data(gaze_direction):
    with open("gaze_logs.txt", "a") as log_file:
        log_file.write(f"{gaze_direction}\n")
