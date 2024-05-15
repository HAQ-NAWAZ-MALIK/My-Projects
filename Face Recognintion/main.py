import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Path to the directory containing training images
image_path = 'Training_images'
images = []
class_names = []

# Get the list of files in the training images directory
file_list = os.listdir(image_path)
print(file_list)

# Load training images and extract class names
for file in file_list:
    current_img = cv2.imread(f'{image_path}/{file}')
    images.append(current_img)
    class_names.append(os.path.splitext(file)[0])

print(class_names)

# Function to find face encodings for the training images
def get_encodings(img_list):
    encoding_list = []

    for img in img_list:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encoding_list.append(encode)
    return encoding_list

# Function to mark attendance in a CSV file
def mark_attendance(name):
    with open('Attendance.csv', 'r+') as file:
        data_list = file.readlines()

        name_list = []
        for line in data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            time_string = now.strftime('%H:%M:%S')
            file.writelines(f'\n{name},{time_string}')

# Get face encodings for the training images
encoded_faces = get_encodings(images)
print('Encoding Complete')

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    # Resize the frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Find faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare the face encoding with known encodings
        matches = face_recognition.compare_faces(encoded_faces, face_encoding)
        face_distances = face_recognition.face_distance(encoded_faces, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = class_names[best_match_index].upper()
            # Draw a rectangle around the face and display the name
            top, right, bottom, left = face_location
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            mark_attendance(name)

    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
