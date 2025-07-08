import face_recognition
import cv2
import os

known_faces = []
known_names = []

# Load known faces
for filename in os.listdir("known_faces"):
    image = face_recognition.load_image_file(f"known_faces/{filename}")
    encoding = face_recognition.face_encodings(image)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        if True in matches:
            name = known_names[matches.index(True)]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()