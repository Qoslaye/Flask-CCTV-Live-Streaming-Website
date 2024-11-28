# CCTV Live Streaming Website Using Flask

This project is a Flask-based web application that streams live footage from a CCTV or IP camera. The app uses OpenCV to capture video frames and serves them dynamically to the web browser.

## Features

- Streams live CCTV footage to a web page.
- Lightweight and easy to set up.
- Supports webcam or IP camera streams.
- Built using Flask and OpenCV.

## How It Works

1. **Backend**:
   - OpenCV (`cv2`) is used to capture video frames from the camera.
   - Frames are encoded in JPEG format and sent to the browser as a video stream using Flask.

2. **Frontend**:
   - An HTML template (`index.html`) is used to display the live video feed.

## Installation and Setup

### Prerequisites
- Python 3.x
- Pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Qoslaye/Flask-CCTV-Live-Streaming-Website.git
   cd Flask-CCTV-Live-Streaming-Website
