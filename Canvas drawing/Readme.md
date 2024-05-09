---

# Canvas Project

This project is a simple canvas application that allows you to draw using hand gestures captured through your webcam.
![video](canvas.mp4)

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Mediapipe (`mediapipe`)
- Collections (`collections`)

## Installation

You can install the required packages using pip:

```bash
pip install opencv-python numpy mediapipe
```

## Usage

1. Clone or download the project repository.
2. Install the required packages as mentioned above.
3. Run the `canvas.py` script using Python.
4. Use your hand gestures to draw on the canvas.

## Features

- Supports drawing in multiple colors: blue, green, red, and yellow.
- Includes a clear button to reset the canvas.
- Saves the canvas image as `canvas_image.jpg` when 's' key is pressed.

## How to Draw

- Move your hand in front of the webcam.
- Use your index finger to draw lines on the canvas.
- Select different colors by touching the corresponding rectangles at the top of the canvas.
- Use the clear button to reset the canvas.

## Acknowledgments

This project utilizes OpenCV, Mediapipe, and NumPy libraries to enable real-time hand gesture-based drawing on the canvas.

---
