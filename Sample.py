import cv2
import os

# Ensure paths to necessary files
dataset_dir = "Dataset"  # Directory where user images will be saved
cascade_dir = "Real-Time-Face-verification/xml"  # Directory containing cascade files (default OpenCV cascades)
cascade_files = [f for f in os.listdir(cascade_dir) if f.endswith('.xml')]  # List all .xml files

# Initialize a list for face cascades
faceCasCades = []

# Load all cascade classifiers from the specified directory
for file in cascade_files:
    cascade_path = os.path.join(cascade_dir, file)
    faceCascade = cv2.CascadeClassifier(cascade_path)
    if faceCascade.empty():
        print(f"[ERROR] Haar cascade file {file} not loaded correctly.")
    else:
        faceCasCades.append(faceCascade)

# Ensure the dataset directory exists
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Initialize video capture
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cam.isOpened():
    print("[ERROR] Unable to access the camera.")
    exit()

# Define minimum window size for face detection
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# Prompt for user name and ID
user_name = input("Enter your name: ")
user_id = input("Enter a numeric ID: ")

# Create a directory for the user within the dataset
user_dir = os.path.join(dataset_dir, f"User_{user_id}")
if not os.path.exists(user_dir):
    os.makedirs(user_dir)

# Get the current photo count in the user's directory
existing_photos = len([f for f in os.listdir(user_dir) if f.endswith('.jpg')])
photo_count = existing_photos  # Start from the existing count

print(f"\n[INFO] Starting photo collection for {user_name} (ID: {user_id}). Press 'ESC' to exit.")
print(f"[INFO] {existing_photos} existing photos found. Continuing from there.")

while True:
    ret, img = cam.read()
    if not ret:
        print("[ERROR] Unable to read from camera.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = []
    for faceCascade in faceCasCades:
        # Detect faces using each cascade
        detected_faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        faces.extend(detected_faces)  # Append results from each cascade

    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Increment photo counter and save image
        photo_count += 1
        photo_path = os.path.join(user_dir, f"{user_id}_{photo_count}.jpg")
        cv2.imwrite(photo_path, gray[y:y + h, x:x + w])
        print(f"[INFO] Photo {photo_count} saved.")

        # Display name and number of photos taken
        cv2.putText(img, f"{user_name} (ID: {user_id})", (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Photos: {photo_count}", (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

    # Display the video feed with face detection
    cv2.imshow('Collecting Photos', img)

    # Exit on pressing 'ESC' or stop after 100 photos
    k = cv2.waitKey(10) & 0xff
    if k == 27 or photo_count >= existing_photos + 60:  # Allow however many additional photos
        break

# Cleanup
print("\n[INFO] Exiting Program and cleanup.")
cam.release()
cv2.destroyAllWindows()

