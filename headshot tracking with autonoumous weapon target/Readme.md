```markdown
# Face Detection and Tracking with OpenCV and Arduino Integration

This repository contains two Python scripts that demonstrate face detection and tracking using OpenCV and integration with an Arduino board to control servo motors.

## 1. Face Detection (Facededuction.py)

This script uses the OpenCV library to detect faces in real-time from a webcam feed. It utilizes the Haar Cascade classifier for face detection and draws rectangles around the detected faces in the video stream.

### Prerequisites

- Python
- OpenCV (`cv2`)
- NumPy

### Installation

1. Install OpenCV and NumPy libraries:

```
pip install opencv-python numpy
```

2. Download the Haar Cascade classifier file `haarcascade_frontalface_default.xml` and place it in the same directory as the script.

### Usage

1. Run the script:

```
python Facededuction.py
```

2. The script will open a window displaying the webcam feed with rectangles drawn around any detected faces.
3. Press the 'q' key to exit the program.

### How it Works

1. The script loads the pre-trained Haar Cascade classifier for face detection.
2. It establishes a connection to the default webcam (`cv2.VideoCapture(0)`).
3. In a loop, the script captures frames from the webcam and converts them to grayscale.
4. The `detectMultiScale` function from the Haar Cascade classifier is used to detect faces in the grayscale frame.
5. For each detected face, a rectangle is drawn around it using `cv2.rectangle`.
6. The number of detected faces is displayed on the frame using `cv2.putText`.
7. The processed frame is displayed using `cv2.imshow`.
8. The loop continues until the 'q' key is pressed.
9. Finally, the webcam connection is released, and all OpenCV windows are closed.

## 2. Face Tracking with Arduino Integration (Facetracking.py)

This script uses the OpenCV library to detect and track faces in real-time from a webcam feed. It integrates with an Arduino board to control two servo motors based on the face's position in the video stream.

### Prerequisites

- Python
- OpenCV (`cv2`)
- PyFirmata
- NumPy
- Arduino board

### Installation

1. Install the required libraries:

```
pip install opencv-python pyfirmata numpy
```

2. Connect the Arduino board to your computer via USB.
3. Ensure that the servo motors are connected to the appropriate pins on the Arduino board (in this case, pins 9 and 10).

### Usage

1. Update the `port` variable in the script to match the serial port of your Arduino board.
2. Run the script:

```
python Facetracking.py
```

3. The script will open a window displaying the webcam feed.
4. If a face is detected, it will be tracked, and the servo motors will move accordingly to follow the face's position.
5. Press 'q' to exit the program.

### How it Works

1. The script establishes a connection to the webcam and sets the resolution.
2. It initializes the FaceDetector module from the `cvzone` library for face detection.
3. The PyFirmata library is used to establish communication with the Arduino board and control the servo motors.
4. In a loop, the script captures frames from the webcam and uses the FaceDetector module to detect faces.
5. If a face is detected, its center coordinates are calculated, and these coordinates are used to determine the desired servo positions using interpolation.
6. The servo positions are sent to the Arduino board using the PyFirmata library, and the servo motors move accordingly.
7. The frame is displayed with visual indicators (circles, lines, and text) showing the face position and servo angles.
8. The loop continues until the 'q' key is pressed.
9. Finally, the webcam connection is released, and the OpenCV window is closed.

Note: Make sure to have the required hardware (Arduino board and servo motors) properly connected and configured before running the `Facetracking.py` script.
```
