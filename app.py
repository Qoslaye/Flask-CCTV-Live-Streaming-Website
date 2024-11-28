from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the camera (use 0 for the default webcam or an IP camera stream URL)
camera = cv2.VideoCapture(0)  # Replace 0 with 'http://your-ip-camera-stream-url' for IP cameras


def cctv_live():
    while True:
        success, frame = camera.read()
        if not success:
            # Handle failure to read frame
            print("Failed to capture video frame")
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                print("Failed to encode frame")
                break
            frame = buffer.tobytes()

            # Yield the frame to the response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    # Render the main HTML template
    return render_template('index.html')


@app.route('/video')
def video():
    # Stream the video feed
    return Response(cctv_live(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
