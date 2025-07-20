import cv2
import os

# ====== CONFIGURATION ======
video_path = 'mendoza1.mp4'  # Path to your video file
output_folder = 'frames_raw'       # Folder to save frames
interval_seconds = 0.3         # Capture a frame every X seconds
# ============================

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
frame_interval = int(fps * interval_seconds)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Video FPS: {fps}, Total Frames: {total_frames}")
print(f"Capturing one frame every {interval_seconds} seconds ({frame_interval} frames interval).")

frame_count = 0
image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"{image_count}.png")
        cv2.imwrite(filename, frame)
        image_count += 1

    frame_count += 1

cap.release()
print("Done.")