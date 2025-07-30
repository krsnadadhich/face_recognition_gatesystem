import face_recognition
import cv2
import pickle
import os

def register_resident():
    name = input("Enter your name: ").strip()
    cap = cv2.VideoCapture(0)

    print("Capturing face. Look at the camera...")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Press 's' to capture face", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    cap.release()
    cv2.destroyAllWindows()

    face_encodings = face_recognition.face_encodings(frame)
    if not face_encodings:
        print("No face found! Try again.")
        return

    encoding = face_encodings[0]

    with open(f"residents/{name}.pkl", 'wb') as f:
        pickle.dump(encoding, f)

    print(f"{name} registered successfully!")

if __name__ == "__main__":
    if not os.path.exists("residents"):
        os.makedirs("residents")
    register_resident()
