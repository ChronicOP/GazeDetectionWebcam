# Gaze Tracking System

This project is a **Gaze Tracking System** that detects facial landmarks and determines eye gaze direction, including left, right, up, and down. It uses OpenCV and Dlib for face and eye detection and requires a pre-trained model for landmark detection.

---

## Features

- **Real-time Gaze Detection**: Determines gaze direction (left, right, up, down, or center).
- **Robust Face and Eye Detection**: Uses Dlib's landmark predictor for precise detection.
- **Cross-platform**: Works on multiple platforms with Python and OpenCV.

---

## Prerequisites

### Required Libraries

Install the necessary dependencies using:

```bash
pip install opencv-python dlib numpy
```

### Pre-trained Model

Download the `shape_predictor_68_face_landmarks.dat` model [here](https://github.com/davisking/dlib-models).

Place the model file in the same directory as your project.

---

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gaze-tracking-system.git
   cd gaze-tracking-system
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python main.py
   ```

4. Ensure your webcam is working for live testing.

---

## Demonstration

### Video Example

Below is a demonstration video of the system in action:

[Watch the demonstration video]:--> ([https://your-video-link.com/demo.mp4](https://drive.google.com/file/d/1HqcEDdQW5IfOlafkeWf2a-4DX0i2J9h9/view?usp=sharing))


---

## File Structure

```
.
├── main.py
├── gaze_tracking.py
├── requirements.txt
├── shape_predictor_68_face_landmarks.dat
├── README.md
```

---

## How It Works

1. Captures a video feed using OpenCV.
2. Detects face and eyes using Dlib's frontal face detector.
3. Analyzes eye regions to compute the gaze direction.
4. Displays the gaze direction (left, right, up, down, center) on the live feed.

---

## Troubleshooting

- Ensure the `shape_predictor_68_face_landmarks.dat` file is correctly downloaded and placed in the project directory.
- Verify your camera permissions and functionality.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or report issues.

---

## License

This project is licensed under the MIT License.
