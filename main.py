import cv2, os
from contact_options import send_email

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

message_sent = False

while True:
    rec, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) > 0 and not message_sent:
        cv2.imwrite("face.jpg", frame)

        #* Send the image via email
        if send_email("face.jpg"):
            os.remove("face.jpg")  #* Delete the image after sending
            print("Image deleted from local directory.")
            message_sent = True
        
    cv2.imshow("Face Detection", frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()