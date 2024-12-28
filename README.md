Gaze Tracking System

This project implements a real-time gaze tracking system using OpenCV, dlib, and Python. The application detects a user's face, identifies their eyes, and determines the direction they are looking: left, right, up, down, or center.

Features

Real-Time Gaze Detection: Detects the user's gaze direction in real time.

Eye Landmark Detection: Uses dlib's 68-face landmarks to locate and analyze the eyes.

Direction Analysis: Determines whether the user is looking left, right, up, down, or center.

Visual Feedback: Displays the gaze direction and eye landmarks on the video feed.

Requirements

Ensure the following dependencies are installed:

Python 3.7 or higher

OpenCV

dlib

NumPy

Install them using the following command:

pip install opencv-python dlib numpy

Setup Instructions

Step 1: Download Pre-trained Model

This project uses dlib's 68-face landmark predictor. Download the pre-trained model shape_predictor_68_face_landmarks.dat from the following link:

Download shape_predictor_68_face_landmarks.dat

After downloading, extract the file and place it in the root directory of the project.

Step 2: Clone the Repository

Clone the project repository to your local machine:

git clone https://github.com/yourusername/gaze-tracking-project.git
cd gaze-tracking-project

Step 3: Run the Application

Run the application using the following command:

python main.py

Project Structure

|-- main.py                # Main application script
|-- gaze_tracking.py       # Gaze tracking logic
|-- shape_predictor_68_face_landmarks.dat # Pre-trained model

How It Works

Face Detection: Detects the user's face in the video feed using dlib's frontal face detector.

Eye Extraction: Identifies eye regions based on the 68-face landmark model.

Gaze Analysis: Analyzes the position of the iris in relation to the eye to determine gaze direction.

Real-Time Feedback: Displays gaze direction and eye landmarks on the video feed.

Known Issues

The system may not work effectively in low-light conditions.

Glasses or extreme head movements may affect accuracy.

Future Enhancements

Add calibration for individual users to improve accuracy.

Include support for detecting blinks and closed eyes.

Enhance robustness to varying lighting conditions.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments

dlib Library

OpenCV Documentation

Contact

For any questions or suggestions, please contact:

Name: Your Name

Email: your.email@example.com

Enjoy using the gaze tracking system!
