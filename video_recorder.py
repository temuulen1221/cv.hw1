import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for .avi file
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Output file, FPS, resolution

recording = False
print("Video Record started. Press SPACE to Record/Pause, ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    if recording:
        out.write(frame)
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)
    
    cv2.imshow('Video Recorder', frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == 32:
        recording = not recording
        status = "Recording" if recording else "Paused"
        print(f"Mode changed to: {status}")
    
    elif key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Record ended. Video saved as 'output.avi'.")