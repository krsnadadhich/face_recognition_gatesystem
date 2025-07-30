# 🧠 Face Recognition Gate System

A Python-based biometric gate system that uses facial recognition to identify residents and trigger gate access. Designed for secure and automated residential entry.

---

## 🚀 Features

- 🔒 Detects and recognizes faces in real-time  
- 👥 Maintains a face encoding database (`.pkl` files)  
- 🎥 Uses live webcam input for identification  
- 🚪 Triggers gate logic (print/open simulation)  
- 🧠 Built using OpenCV and face_recognition libraries

---

## 🗂️ Project Structure

```
face_recognition_gatesystem/
├── main.py               # Entry point for face detection and gate logic
├── encode_residents.py   # Script to encode and save new faces
├── residents/            # Folder containing encoded resident .pkl files
├── README.md             # Project overview
└── requirements.txt      # Required Python packages
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/krsnadadhich/face_recognition_gatesystem.git
cd face_recognition_gatesystem
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, I’ll help you generate one.

### 3. Encode Faces
Add new face images to the encoding script and run:
```bash
python encode_residents.py
```

### 4. Start the System
```bash
python main.py
```

---

## 📸 How it Works

1. Captures live video frames  
2. Detects face using the webcam  
3. Compares the detected face with stored `.pkl` encodings  
4. If matched → simulates gate open  
5. If not matched → access denied

---

## 📦 Technologies Used

- Python  
- OpenCV  
- face_recognition  
- pickle  
- NumPy

---

## 🧪 Future Improvements

- Hardware integration for real gate control (e.g., Arduino/Raspberry Pi)  
- Admin UI for managing residents  
- SMS/Email notifications

---

## 🧑‍💻 Author

**Krishna Dadhich**  
GitHub: [@krsnadadhich](https://github.com/krsnadadhich)
