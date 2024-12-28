import cv2
import dlib
import numpy as np


class GazeTracking:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("/Users/prathameshpatil/Desktop/shape_predictor_68_face_landmarks.dat")
    def detect_face_and_eyes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        for face in faces:
            landmarks = self.predictor(gray, face)
            left_eye_points = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]
            right_eye_points = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]
            return left_eye_points, right_eye_points
        return None, None

    def get_eye_region(self, frame, eye_points):
        min_x = min([point[0] for point in eye_points])
        max_x = max([point[0] for point in eye_points])
        min_y = min([point[1] for point in eye_points])
        max_y = max([point[1] for point in eye_points])
        return frame[min_y:max_y, min_x:max_x]

    def analyze_gaze(self, frame, left_eye_points, right_eye_points):
        if left_eye_points and right_eye_points:
            left_eye_region = self.get_eye_region(frame, left_eye_points)
            right_eye_region = self.get_eye_region(frame, right_eye_points)

            left_gaze = self.get_gaze_direction(left_eye_region)
            right_gaze = self.get_gaze_direction(right_eye_region)

            # Combine gaze information from both eyes
            if left_gaze == "left" or right_gaze == "left":
                return "left"
            elif left_gaze == "right" or right_gaze == "right":
                return "right"
            elif left_gaze == "up" or right_gaze == "up":
                return "up"
            elif left_gaze == "down" or right_gaze == "down":
                return "down"
            else:
                return "center"
        return None

    def get_gaze_direction(self, eye_region):
        gray_eye = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY)
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(threshold_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            # Find the largest contour (assuming it's the iris)
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(largest_contour)

            # Determine gaze direction based on iris position
            height, width = eye_region.shape[:2]
            iris_x = x + w // 2
            iris_y = y + h // 2

            # Correcting left-right logic
            if iris_x < width // 3:
                return "right"  # Swapped
            elif iris_x > 2 * width // 3:
                return "left"  # Swapped
            elif iris_y < height // 3:
                return "up"
            elif iris_y > 2 * height // 3:
                return "down"
            else:
                return "center"
        return "center"


def main():
    gaze_tracker = GazeTracking()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        left_eye_points, right_eye_points = gaze_tracker.detect_face_and_eyes(frame)
        if left_eye_points and right_eye_points:
            gaze_direction = gaze_tracker.analyze_gaze(frame, left_eye_points, right_eye_points)
            cv2.putText(frame, f"Gaze: {gaze_direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw eye landmarks
            for point in left_eye_points + right_eye_points:
                cv2.circle(frame, point, 2, (255, 0, 0), -1)

        cv2.imshow("Gaze Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
