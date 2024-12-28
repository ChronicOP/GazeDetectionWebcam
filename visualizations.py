import cv2
import numpy as np

def draw_gaze_vector(frame, pupil, gaze_vector, color=(0, 255, 0)):
    if not pupil:
        return frame
    start_point = (int(pupil[0]), int(pupil[1]))
    end_point = (
        int(pupil[0] + gaze_vector[0] * 100),
        int(pupil[1] + gaze_vector[1] * 100)
    )
    cv2.line(frame, start_point, end_point, color, 2)
    cv2.circle(frame, start_point, 5, color, -1)

def annotate_frame(frame, face, pupils, gaze_vector, gaze_direction):
    for i, pupil in enumerate(pupils):
        if pupil:
            draw_gaze_vector(frame, pupil, gaze_vector)

    cv2.putText(frame, f"Gaze: {gaze_direction}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return frame
