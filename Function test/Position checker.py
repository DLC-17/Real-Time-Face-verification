import cv2

import os

# Define the path to trainer.yml
trainer_path = os.path.join("xml", "trainer.yml")

# Check if the file exists
if os.path.exists(trainer_path):
    print(f"[INFO] Trainer file found at: {trainer_path}")
else:
    print(f"[ERROR] Trainer file not found at: {trainer_path}")
