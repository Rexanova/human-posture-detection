# Human Posture Detection Web App

## Overview

An end-to-end real-time human posture detection system built using YOLOv8, Flask, and OpenCV.
Developed as part of a Final Year Diploma Capstone Project, this application uses a live webcam feed to detect and classify posture as Good or Bad, providing instant visual and audio feedback.

---

## Features

* Real-time posture detection via webcam
* YOLOv8-based deep learning model
* Good vs Bad posture classification
* Bounding box visualization (toggle option available)
* Audio alert for incorrect posture
* Flask-based web interface

---

## Output & Demo

<img width="743" height="372" alt="image" src="https://github.com/user-attachments/assets/e08edecb-5cef-4b5b-b9d4-634b3184375b" />
<img width="743" height="372" alt="image" src="https://github.com/user-attachments/assets/f0244cf3-35c4-4dee-9a9d-8c929b04791d" />
<img width="743" height="372" alt="image" src="https://github.com/user-attachments/assets/9ee4e7a1-54c3-4b8f-9c50-2cafc0061fde" />
<img width="743" height="372" alt="image" src="https://github.com/user-attachments/assets/517e5761-3815-43ad-a814-db2e948a462d" />

The application performs real-time posture detection directly in the browser.

### What You See

* Live webcam stream displayed on a web page
* Posture classification updated frame-by-frame
* Green box indicates Good posture
* Red box indicates Bad posture
* Audio alert triggered for incorrect posture

---

## Tech Stack

* Python
* Flask
* OpenCV
* Ultralytics YOLOv8

---

## Project Structure

```id="w9s3k1"
human-posture-detection/
│
├── app.py                # Main Flask application
├── posture.yaml          # Dataset configuration
├── app.ipynb             # Model experimentation
│
├── templates/            # HTML frontend
├── static/               # CSS, JS, audio files
├── train/                # Model weights and training outputs
```

---

## Installation & Setup

### 1. Clone the repository

```id="8nq4cx"
git clone https://github.com/Rexanova/human-posture-detection.git
cd human-posture-detection
```

### 2. Install dependencies

```id="0tpnhq"
pip install -r requirements.txt
```

### 3. Run the application

```id="3a6df0"
python app.py
```

### 4. Open in browser

```id="y9c2lm"
http://127.0.0.1:5000/
```

---

## How It Works

* Webcam captures live video frames
* Frames are processed using the YOLOv8 model
* The model predicts posture class (Good / Bad)
* Bounding boxes and labels are drawn on the frame
* Flask streams processed frames to the frontend
* Audio alert is triggered for incorrect posture

---

## Notes

* Ensure your webcam is enabled
* Make sure model weights (`best.pt`) are available in the correct directory
* Good lighting improves detection accuracy

---

## Future Improvements

* Mobile compatibility
* Posture analytics dashboard
* Model optimization for faster inference
* Cloud deployment

---

## Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

---

## Author

Musfirah Shaikh, Final Year Diploma Capstone Project,
Currently pursuing BTech in Engineering
GitHub: https://github.com/Rexanova
