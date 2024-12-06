import cv2
import numpy as np
from PIL import Image
import os

# Path for face image database
path = "Dataset"
# Initialize the recognizer and face detector
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if detector.empty():
    print("[ERROR] Could not load Haar cascade.")
    exit()
def getImagesAndLabels(base_path):
    """
    Function to traverse through folders in the dataset directory, extract face images, 
    and their associated labels for training.
    """
    face_samples = []
    ids = []

    # Traverse all subdirectories and files in the base_path
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.jpg'):  # Process only .jpg files
                try:
                    image_path = os.path.join(root, file)
                    # Convert the image to grayscale
                    PIL_img = Image.open(image_path).convert('L')
                    img_numpy = np.array(PIL_img, 'uint8')

                    # Extract the user ID from the filename
                    id = int(file.split('_')[0])  # Filename format: <id>_<count>.jpg
                    
                    # Detect faces in the image
                    faces = detector.detectMultiScale(img_numpy)
                    
                    # Add each detected face and its label
                    for (x, y, w, h) in faces:
                        face_samples.append(img_numpy[y:y + h, x:x + w])
                        ids.append(id)
                except Exception as e:
                    print(f"[ERROR] Could not process file {file}: {e}")
    
    return face_samples, ids

# Start training process
print("\n [INFO] Training faces. It will take a few seconds. Wait ...")

faces, ids = getImagesAndLabels(path)

if faces and ids:
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    if not os.path.exists('trainer'):
        os.makedirs('trainer')

    recognizer.write('trainer/trainer.yml')

    # Print the number of faces trained and exit
    print(f"\n [INFO] {len(np.unique(ids))} unique IDs trained. Exiting Program.")
else:
    print("\n [INFO] No faces found in the dataset. Exiting Program.")
