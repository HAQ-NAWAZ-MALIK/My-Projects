import cv2
import numpy as np
import pyautogui
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Initialize camera
cap = cv2.VideoCapture(0)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize screen size
screen_width, screen_height = pyautogui.size()

# Define gesture thresholds
click_threshold = 20
scroll_threshold = 50

# Define smoothing factor
smoothing_factor = 0.5

# Initialize previous cursor position
prev_cursor_pos = None

while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get index finger tip position
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_pos = (int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0]))

            # Get thumb tip position
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_pos = (int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0]))

            # Get little finger tip position
            little_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            little_finger_pos = (int(little_finger_tip.x * frame.shape[1]), int(little_finger_tip.y * frame.shape[0]))

            # Get middle finger tip position
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            middle_finger_pos = (int(middle_finger_tip.x * frame.shape[1]), int(middle_finger_tip.y * frame.shape[0]))

            # Move cursor smoothly
            if prev_cursor_pos is None:
                prev_cursor_pos = index_finger_pos
            else:
                cursor_pos = (
                    prev_cursor_pos[0] + smoothing_factor * (index_finger_pos[0] - prev_cursor_pos[0]),
                    prev_cursor_pos[1] + smoothing_factor * (index_finger_pos[1] - prev_cursor_pos[1])
                )
                screen_pos = (
                    int(cursor_pos[0] / frame.shape[1] * screen_width),
                    int(cursor_pos[1] / frame.shape[0] * screen_height)
                )
                pyautogui.moveTo(screen_pos[0], screen_pos[1], duration=0.1)
                prev_cursor_pos = cursor_pos

            # Perform click actions
            if cv2.norm(np.array(index_finger_pos) - np.array(thumb_pos)) < click_threshold:
                pyautogui.click(button='left')
            elif cv2.norm(np.array(thumb_pos) - np.array(little_finger_pos)) < click_threshold:
                pyautogui.click(button='right')

            # Perform scroll actions
            if middle_finger_pos[1] < middle_finger_tip.y * frame.shape[0] - scroll_threshold:
                pyautogui.scroll(50)
            elif middle_finger_pos[1] > middle_finger_tip.y * frame.shape[0] + scroll_threshold:
                pyautogui.scroll(-50)

            # Draw hand landmarks on frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display frame
    cv2.imshow('Virtual Mouse', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()