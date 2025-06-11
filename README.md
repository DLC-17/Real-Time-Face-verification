# 🧑‍🤝‍🧑 Real-Time Face Recognition System

This project implements a real-time face recognition system using OpenCV's LBPHFaceRecognizer. It enables capturing user photos, training a facial recognition model, and recognizing faces in live video streams.

Inspired by the [Real-Time Face Recognition: An End-To-End Project](https://www.marcelo-rovai.com/) by Marcelo Rovai, this project incorporates foundational concepts and extends them for robust, real-time performance.

---

## 🚀 Features

- Capture and store face images for multiple users  
- Train a facial recognition model using the Local Binary Pattern Histogram (LBPH) algorithm  
- Utilize multiple Haar cascade classifiers for reliable face detection (frontal and side profiles)  
- Real-time face recognition with user names and confidence levels displayed  
- Support dynamic addition of new users without overwriting existing data  

---

## 🛠 Setup Instructions

### 1. Clone the Repository
    Make sure you have Python 3.x installed. Then install required libraries:
    pip install opencv-python opencv-contrib-python numpy

2. Install Dependencies
Make sure you have Python 3.x installed. Then install required libraries:
```bash
  pip install opencv-python opencv-contrib-python numpy
```
4. Prepare Haar Cascade Files
Ensure the Haar cascade XML files are located in the Real-Time/xml/ directory. If missing, download them from the OpenCV GitHub Haar Cascades.

⚙️ Usage
(a) Capture User Photos
Run the script to collect face images:
    
    python collect_photos.py
You will be prompted to enter a user name and a unique numeric ID. Photos will be saved in the Dataset/ directory.

(b) Train the Model
Train the LBPH face recognizer on the collected photos:
    
     python train_model.py
This generates a trained model file trainer.yml saved in the trainer/ directory.

(c) Run Real-Time Recognition
Start the live face recognition system:
    
    python recognize_faces.py
Faces will be detected and recognized in real-time from the webcam feed.

📂 Project Structure

├── Dataset/                 # Captured user face images  
├── Real-Time/  
│   ├── xml/                 # Haar cascade XML files for face detection  
│   ├── trainer/             # Trained model file (trainer.yml)  
├── collect_photos.py        # Script to capture user photos  
├── train_model.py           # Script to train the face recognition model  
├── recognize_faces.py       # Script for real-time face recognition  
├── requirements.txt         # Python dependencies  

🙏 Acknowledgments
This project is heavily inspired by Marcelo Rovai's Real-Time Face Recognition: An End-To-End Project. Many thanks for their clear explanations and guidance.

🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests for improvements or new features.

📄 License
This project is open source under the MIT License. See the LICENSE file for details.






