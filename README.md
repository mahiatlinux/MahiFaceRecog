# MahiFaceRecog
This code is a simple face recognition program made with Python. It uses the face_recognition library and OpenCV. It uses a webcam to capture frames, detects faces in each frame, and compares them with a set of known faces to recognize the person. And for all those people who for some reason can't install the needed libs, I have included a virtual enviroment.
 
Here is a step-by-step explanation of the code: 
 
1. The required libraries, face_recognition and OpenCV, are imported. 
 
2. The paths of the images of the people you want to recognize are specified and stored in lists. These images are used to create face encodings for comparison. 
 
3. The webcam is opened using the cv2.VideoCapture() function. 
 
4. A while loop is started to continuously capture frames from the webcam. 
 
5. Inside the loop, each frame is read using the video_capture.read() function. 
 
6. The face_recognition library is used to find the locations and encodings of all faces in the current frame using the face_recognition.face_locations() and face_recognition.face_encodings() functions. 
 
7. A for loop is used to iterate through each face found in the frame. 
 
8. For each face, the code checks if it matches any of the known faces by comparing the face encodings using the face_recognition.compare_faces() function. 
 
9. If a match is found, the name of the recognized person is assigned. 
 
10. A rectangle is drawn around the face using the cv2.rectangle() function. 
 
11. The name of the recognized person is displayed below the face using the cv2.putText() function. 
 
12. The resulting frame with the recognized faces is displayed using the cv2.imshow() function. 
 
13. The loop continues until the 'q' key is pressed, which breaks the loop. 
 
14. After the loop ends, the webcam is released using the video_capture.release() function and all windows are closed using the cv2.destroyAllWindows() function.
