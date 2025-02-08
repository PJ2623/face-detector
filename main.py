import cv2
import os
import time

from dotenv import load_dotenv
from contact_options import send_email, send_text_or_whatsapp_message
from utils import upload_image_to_cloudinary

load_dotenv()

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(os.getenv("WEB_CAM_URL"))

message_sent = False  # Flag to prevent multiple messages
last_detection_time = None  # Track last time a face was detected

while True:
    rec, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) > 0:
        last_detection_time = time.time()  # Update detection timestamp
        
        if not message_sent:
            image_path = "face.jpg"
            cv2.imwrite(image_path, frame)  # Capture image

            print("Intruder detected! Uploading image...")
            image_url = upload_image_to_cloudinary(image_path)  # Upload image & get URL

            if image_url:
                print(f"Image uploaded successfully: {image_url}")

                # Send WhatsApp message with image URL
                if send_text_or_whatsapp_message("w", image_url):
                    print("WhatsApp message sent successfully!")

                message_sent = True  # Prevent duplicate alerts

    # Reset after 10 seconds if no face detected
    elif message_sent and last_detection_time and time.time() - last_detection_time > 10:
        print("No intruder detected for 10 seconds. Resetting alert system.")
        message_sent = False
    
    # Draw bounding box around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()