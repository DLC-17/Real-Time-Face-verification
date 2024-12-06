Overview
This project implements a real-time face recognition system that utilizes OpenCV's LBPHFaceRecognizer for training and recognizing faces.
The project allows for capturing user photos, training a model on the dataset, and recognizing faces in live video streams.

This project is inspired by and incorporates foundational concepts and code from the Real-Time Face Recognition: An End-To-End Project by Marcelo Rovai.

Features:
Captures and stores face images for different users.
Trains a facial recognition model using the Local Binary Pattern Histogram (LBPH) algorithm.
Uses multiple Haar cascade classifiers for robust face detection (including frontal and side profiles).
Recognizes and displays user names with confidence levels in real-time.
Supports adding new users dynamically without overwriting existing data.

Setup Instructions:
Follow these steps to get started with the project:

1. Clone the Repository

bash
git clone https://github.com/DLC-17/Real-Time-Face-verification.git
cd real-time-face-recognition
2. Install Dependencies
Ensure Python 3.x is installed. Then, install the required Python libraries:

bash
pip install opencv-python opencv-contrib-python numpy
3. Prepare Haar Cascade Files
Ensure the Haar cascade XML files are available in the specified directory:

bash
Real-Time/xml/
If the files are missing, download them from OpenCV's GitHub: Haar Cascades.
Ensure that all files have the neccessary directions to relevant directories and files

4. Run the Components
  (a) Collect User Photos
To collect photos of users, run:
python collect_photos.py
Enter the user's name and a unique numeric ID when prompted.
Photos will be saved in the Dataset/ directory.

  (b) Train the Model
Train the facial recognition model with the collected photos:
python train_model.py
This will generate a file trainer.yml in the trainer/ directory.

  (c) Run Real-Time Recognition
Finally, recognize faces in a live video stream:
python recognize_faces.py

Project Structure:
├── Dataset/                # Stores captured user face images
├── Real-Time/
│   ├── xml/                # Haar cascade files for face detection
│   ├── trainer/            # Contains trained model file (trainer.yml)
├── collect_photos.py       # Script for capturing user photos
├── train_model.py          # Script for training the facial recognition model
├── recognize_faces.py      # Script for real-time face recognition
├── requirements.txt        # Python dependencies

Acknowledgments:
This project is heavily inspired by the excellent work outlined in the Real-Time Face Recognition: An End-To-End Project. 
Many thanks to the authors for their detailed explanations and implementation guidance.

Contributing:
Contributions are welcome! Feel free to fork the repository and create pull requests for improvements or additional features.

License:
This project is open-source and available under the MIT License. See the LICENSE file for details.






