import cv2
import os

# Path to the MP4 file
video_file_path = 'GX020083.MP4'

# Open the video file
cap = cv2.VideoCapture(video_file_path)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Directory where you want to save the images
save_dir = './images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Read the frame rate of the video to determine how often to capture images
fps = cap.get(cv2.CAP_PROP_FPS)

# Initialize frame count
frame_count = 0

while True:
    # Read the next frame from the video
    success, frame = cap.read()

    # If read was unsuccessful, we've reached the end of the video
    if not success:
        break

    # Capture an image every second
    if frame_count % int(fps) == 0:
        # Construct image name
        image_name = os.path.join(save_dir, f'image_{frame_count // int(fps)}.png')
        # Save the image
        cv2.imwrite(image_name, frame)
        print(f'Saved {image_name}')

    frame_count += 1

# Release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()
