import cv2  # Import the OpenCV library for computer vision tasks
import numpy as np  # Import the NumPy library for numerical operations
import time  # Import the time library for time-related tasks

# Load the pre-trained face classifier
faceClassifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open a connection to the webcam
videoCam = cv2.VideoCapture(0)

# Check if the webcam can be accessed
if not videoCam.isOpened():
    print("Camera cannot be accessed")
    exit()

# Initialize a flag to control the loop
isQPressed = False
while not isQPressed:
    # Read a frame from the webcam
    ret, frame = videoCam.read()

    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the grayscale frame
        faces = faceClassifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the number of faces detected
        text = "faces detected = " + str(len(faces))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (0, 30), font, 1, (255, 0, 0), 1)

        # Show the frame with detected faces
        cv2.imshow("Haq_omar", frame)
        # Check if the 'q' key is pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            isQPressed = True
            break

# Release the webcam and close all OpenCV windows
videoCam.release()
cv2.destroyAllWindows()
