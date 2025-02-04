import os

import smtplib
import pywhatkit
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from dotenv import load_dotenv

load_dotenv()

def send_email(image):
    """Send an email with the image attached."""
    
    try:
        message = MIMEMultipart()
        message["From"] = os.getenv("SENDER_EMAIL")
        message["To"] = os.getenv("RECIPIENT_EMAIL")
        message["Subject"] = "Security Alert, Intruder Detected!"
        
        #*Attach the image to the email
        with open(image, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(image)}",
            )
            message.attach(part)
        
        #*Connect to the email server
        with smtplib.SMTP_SSL(host="smtp.mail.yahoo.com", port=465) as server:
            server.login(os.getenv("SENDER_EMAIL"), os.getenv("SENDER_PASSWORD"))
            server.sendmail(os.getenv("SENDER_EMAIL"), os.getenv("RECIPIENT_EMAIL"), message.as_string())
        
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    

def send_whatsapp_message(image="face.jpg"):
    """Send a WhatsApp message with the image attached."""
    
    try:
        pywhatkit.sendwhats_image(receiver= os.getenv("RECIPIENT_PHONE_NUMBER"),
                                  caption="Security Alert, Intruder Detected!",
                                  img_path=os.path.abspath(image),
                                  tab_close=True,
                                  wait_time=15)
        print("WhatsApp message sent successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")