
---

# Virtual Mouse using Hand Gestures

This Python script utilizes the MediaPipe library and OpenCV to create a virtual mouse controlled by hand gestures. It enables users to control their computer's mouse cursor, perform left and right clicks, and scroll using hand movements captured through the camera.

## Prerequisites

Make sure you have the following libraries installed:
- OpenCV (`cv2`)
- NumPy (`numpy`)
- PyAutoGUI (`pyautogui`)
- MediaPipe (`mediapipe`)

You can install these libraries using pip:
```bash
pip install opencv-python numpy pyautogui mediapipe
```

## Usage

1. Run the script `virtual_mouse.py`.
2. Position your hand in front of the camera.
3. Use your index finger to move the cursor.
4. Perform gestures to trigger left and right clicks.
5. Scroll by moving your middle finger up or down.

### Gesture Thresholds

- Click Threshold: 20 (adjust as needed)
- Scroll Threshold: 50 (adjust as needed)

### Smoothing Factor

A smoothing factor of 0.5 is used to ensure smooth cursor movements. You can adjust this value based on your preference.

## Controls

- Move Cursor: Index Finger
- Left Click: Index Finger + Thumb Touch
- Right Click: Thumb Touch + Little Finger Touch
- Scroll Up/Down: Middle Finger Movement

## Dependencies

- Python 3.x
- OpenCV
- NumPy
- PyAutoGUI
- MediaPipe

## Notes

- Press 'q' to quit the program.
- Ensure proper lighting and hand visibility for accurate detection.
- Adjust thresholds and smoothing factor for optimal performance.

---

Feel free to modify the content as per your requirements or add any additional information you think would be helpful.
