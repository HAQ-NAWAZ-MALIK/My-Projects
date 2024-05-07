import cv2
from pynput.keyboard import Controller
import handtrackingmodule2 as htm

#############
secondary_camera_index = 1  # Set the index of your secondary camera
primary_camera_index = 0    # Set the index of your primary camera

cap = cv2.VideoCapture(secondary_camera_index)
if not cap.isOpened():
    print("Secondary camera not found. Switching to primary camera.")
    cap = cv2.VideoCapture(primary_camera_index)
cap.set(3, 640)
cap.set(4, 480)
#############
detector = htm.handDetector(maxHands=1, detectionCon=0.5, trackCon=0.5)
##############
keyboard = Controller()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        print(fingers)
        
        if fingers[1] == 1:
            keyboard.release('s')
        if fingers[1] == 0:
            keyboard.press("w")
            keyboard.release('s')
        else:
            keyboard.press("s")
            keyboard.release('w')
        
        if fingers[0] == 0:
            keyboard.press("a")
        else:
            keyboard.release('a')
        
        if fingers[4] == 1:
            keyboard.press("d")
        else:
            keyboard.release('d')
    
    cv2.imshow('Game Control', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()