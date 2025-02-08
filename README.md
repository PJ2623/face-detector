# Intruder Detection & Notification System 🚨

This project is an **intruder detection system** that uses **OpenCV** and an **IP Webcam** to detect faces and send **WhatsApp alerts** with an image of the intruder. The captured image is uploaded to **Cloudinary**, and the system prevents duplicate alerts by resetting after a set time.

---

## 🛠️ Features

- 📷 **IP Webcam Integration** – Captures video feed from an Android phone running [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam).
- 🧠 **Face Detection** – Uses OpenCV's Haar Cascade classifier.
- ☁️ **Cloudinary Upload** – Captured images are uploaded to Cloudinary for secure storage.
- 📩 **WhatsApp & Email Alerts** – Alerts are sent via **Twilio WhatsApp API** and email.
- 🛑 **Duplicate Alert Prevention** – Sends only **one alert per detection** and resets after **10 seconds** of no detection.
- 🎭 **Real-time Bounding Boxes** – Draws rectangles around detected faces.

---

## 📸 How It Works

1. **Start the IP Webcam App** on your Android device.
2. Note the **IP Address & Port** shown (e.g., `http://192.168.1.100:8080`).
3. Set the **WEB_CAM_URL** in your `.env` file.
4. Run `main.py` – The script captures frames, detects faces, and sends alerts.
5. If an **intruder is detected**, an image is:
   - Saved temporarily (`face.jpg`).
   - Uploaded to **Cloudinary**.
   - Sent via **WhatsApp** with the image link.
   - Deleted locally after sending.

---

## 📦 Installation & Setup

### 🔧 Prerequisites

- **Python 3.x** installed
- An **Android phone** with [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam)
- Accounts for:
  - [Cloudinary](https://cloudinary.com/)
  - [Twilio](https://www.twilio.com/)
  - An **SMTP email provider** (e.g., Yahoo, Gmail)

### 🛠️ Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-username/intruder-detection.git
   cd intruder-detection
