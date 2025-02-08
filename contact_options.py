import os, smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from twilio.rest import Client
from typing import Literal
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
        with smtplib.SMTP(host="smtp.mail.yahoo.com", port=587) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(os.getenv("SENDER_EMAIL"), os.getenv("SENDER_PASSWORD"))
            server.sendmail(os.getenv("SENDER_EMAIL"), os.getenv("RECIPIENT_EMAIL"), message.as_string())
        
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
        
def send_text_or_whatsapp_message(type: Literal["w", "t"] = "t", image_url: str | None = None):
    """Send a text message or a WhatsApp message.

    ### Args:
        type (Literal[t, w]): The type of message to send. 't' for text message and 'w' for WhatsApp message.
        image_url (str): The URL of the image to send in the message.
    """
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    if type == "w":
        
        if not image_url:
            #*Send a text message without an image if no image URL is provided
            send_response = client.messages.create(
                to=f"whatsapp:{os.getenv("RECIPIENT_NUMBER")}",
                from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
                body="Security Alert, Intruder Detected!",
            )
            
            if send_response.sid:
                return True
            else:
                return False

        send_response = client.messages.create(
            to=f"whatsapp:{os.getenv("RECIPIENT_NUMBER")}",
            from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
            body="Security Alert, Intruder Detected!",
            media_url=[image_url]
        )
        
        if send_response.sid:
            return True
        else:
            return False
    elif type == "t":
        send_response = client.messages.create(
            to=os.getenv("RECIPIENT_NUMBER"),
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            body="Security Alert, Intruder Detected!"
        )
        
        if send_response.sid:        
            return True
        else:
            return False