import face_recognition
import cv2
import os
import pickle
import numpy as np

def load_residents():
    known_encodings = []
    known_names = []

    for file in os.listdir("residents"):
        if file.endswith(".pkl"):
            with open(f"residents/{file}", 'rb') as f:
                encoding = pickle.load(f)
                known_encodings.append(encoding)
                known_names.append(file.replace(".pkl", ""))

    return known_encodings, known_names

def recognize_face(known_encodings, known_names):
    cap = cv2.VideoCapture(0)
    print("Scanning for faces...")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Resize and convert BGR to RGB
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


        face_locations = face_recognition.face_locations(rgb_small_frame)
        if not face_locations:
            continue

        try:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        except Exception as e:
            print("Encoding error:", e)
            continue

        if not face_encodings:
            continue


        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]
                print(f"Access Granted: Welcome {name}")
            else:
                print("Access Denied")

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            label = f"{name}" if name != "Unknown" else "Access Denied"
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("Gate Access", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    known_encodings, known_names = load_residents()
    if not known_encodings:
        print("No registered residents. Run register.py first.")
    else:
        recognize_face(known_encodings, known_names)
