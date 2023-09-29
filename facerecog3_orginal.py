# Install the required libraries
# pip install face_recognition opencv-python

import face_recognition
import cv2

# Load images of the people you want to recognize
known_images_maheswar = ["mahi.jpg", "mahi1.png"]  # Add more Maheswar images as needed
known_encodings_maheswar = [face_recognition.face_encodings(face_recognition.load_image_file(img))[0] for img in known_images_maheswar]

known_images_sidharth = ["sidhu.jpg", "sidhu1.png"]  # Add more Sidharth images as needed
known_encodings_sidharth = [face_recognition.face_encodings(face_recognition.load_image_file(img))[0] for img in known_images_sidharth]

known_images_kishor = ["kishor.jpg", "kishor1.png"]  # Add more Kishor images as needed
known_encodings_kishor = [face_recognition.face_encodings(face_recognition.load_image_file(img))[0] for img in known_images_kishor]

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any of the known faces for Maheswar
        matches_maheswar = any(face_recognition.compare_faces(known_encodings_maheswar, face_encoding))

        # Check if the face matches any of the known faces for Sidharth
        matches_sidharth = any(face_recognition.compare_faces(known_encodings_sidharth, face_encoding))

        # Check if the face matches any of the known faces for Sidharth
        matches_kishor = any(face_recognition.compare_faces(known_encodings_kishor, face_encoding))

        name = "Unknown"
        if matches_maheswar:
            name = "Maheswar"
        elif matches_sidharth:
            name = "Sidharth"
        elif matches_kishor:
            name = "Kishor"

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the name below the face
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
