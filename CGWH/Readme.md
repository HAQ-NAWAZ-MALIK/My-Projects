
---

# Hand Gesture Game Controller

This Python script uses OpenCV and the `pynput` library to create a hand gesture-based game controller. It allows you to control games or applications by detecting hand gestures through your webcam.

## Prerequisites

Ensure you have the following libraries installed:
- OpenCV (`cv2`)
- pynput (`pynput`)
- Hand Tracking Module (`handtrackingmodule2`)

You can install these libraries using pip:
```bash
pip install opencv-python pynput
```

## Usage

1. Set the index of your secondary camera (`secondary_camera_index`) and primary camera (`primary_camera_index`) in the script.
2. Run the script `hand_gesture_game_controller.py`.
3. Position your hand in front of the camera.
4. Use hand gestures to control the game or application.

## Hand Gestures

The script recognizes the following hand gestures:
- Thumb up: Move forward (`w`)
- Thumb down: Move backward (`s`)
- Index finger up: Move left (`a`)
- Pinky finger up: Move right (`d`)

## Controls

- Thumb Up: Forward
- Thumb Down: Backward
- Index Finger Up: Left
- Pinky Finger Up: Right

## Notes

- Ensure proper lighting and hand visibility for accurate gesture detection.
- Modify the script as needed for different games or applications.
- Press 'q' to quit the program.

---

Feel free to modify the content or add any additional information specific to your project.
