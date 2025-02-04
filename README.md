
# Security Monitoring System

### Project Overview
This project is designed to detect faces using a webcam, and send alerts via email and WhatsApp when an intruder is detected. The system captures a snapshot of the scene, attaches the image, and sends it to the specified recipient through both email and WhatsApp. The system uses OpenCV for face detection and pywhatkit for sending WhatsApp messages.

### Features
- Real-time Face Detection: Uses the webcam to detect faces in the video feed.
- Security Alerts: Sends an email with the detected face image when an intruder is detected.
- WhatsApp Notifications: Sends a WhatsApp message with the image as an attachment.
- Email Configuration: The email is sent using the Yahoo SMTP server with SSL encryption for secure communication.
- Environment Configuration: Uses a .env file to store sensitive information, such as email credentials and phone numbers.
### Technologies Used
- OpenCV: For real-time face detection from the webcam feed.
- smtplib: For sending emails via Yahoo's SMTP server.
- pywhatkit: For sending WhatsApp messages.
- dotenv: To load environment variables from a .env file.

# Conclusion
This system provides a basic but effective way to detect intruders in real-time using face detection. It sends security alerts to your email and WhatsApp with an image attachment when a face is detected. The system can be easily extended with additional features such as motion detection, multiple recipient support, or cloud storage integration for saving captured images.

---