import cv2
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Path to the video file
video_path = "C:/Users/vinay/Desktop/project/How to create simple APIs in Node JS.mp4"

# Initialize the video capture
cap = cv2.VideoCapture(video_path)

# Define the time interval between frames (in seconds)
frame_interval = 2  # Adjust this value to change the interval

# Initialize variables
frame_count = 0
last_capture_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Check if it's time to capture a frame
    current_time = time.time()
    if current_time - last_capture_time >= frame_interval:
        # Save the frame as an image
        screenshot_path = f'frame_{frame_count:04d}.png'
        cv2.imwrite(screenshot_path, frame)
        
        # Apply OCR to the screenshot
        text = pytesseract.image_to_string(screenshot_path)
        
        # Print or process the extracted text
        print(f"Frame {frame_count} (at {current_time:.2f}): {text}")
        
        # Update variables
        frame_count += 1
        last_capture_time = current_time
    
# Release the video capture
cap.release()
cv2.destroyAllWindows()