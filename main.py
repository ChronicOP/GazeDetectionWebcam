import cv2
from detection import GazeTracking

def main():
    gaze_tracker = GazeTracking()
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        left_eye_points, right_eye_points = gaze_tracker.detect_face_and_eyes(frame)
        gaze_direction = gaze_tracker.analyze_gaze(frame, left_eye_points, right_eye_points)

        if gaze_direction:
            cv2.putText(frame, f"Gaze Direction: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Gaze Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
