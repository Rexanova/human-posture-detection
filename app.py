from flask import Flask, render_template, Response, request, jsonify
import cv2
from ultralytics import YOLO
from flask import send_file

app = Flask(__name__)

# Load YOLO model
model = YOLO("train/weights/best.pt")
detected_posture = "Detecting..."
show_boxes = True  # Default state for bounding boxes


def generate_frames():
    global detected_posture, show_boxes
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)

        detected_posture = "No Detection"
        for result in results:
            for box in result.boxes:
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = model.names[cls]
                detected_posture = label

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                color = (0, 255, 0) if label == "Good Posture" else (0, 0, 255)

                if show_boxes:  # Only draw boxes if enabled
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_label')
def get_label():
    return jsonify({'posture': detected_posture})


@app.route('/toggle_boxes', methods=['POST'])
def toggle_boxes():
    global show_boxes
    # Get checkbox state from frontend
    show_boxes = request.json.get('showBoxes', True)
    return jsonify({'status': 'success', 'showBoxes': show_boxes})


@app.route('/alert_sound')
def alert_sound():
    # Path to your MP3 file on the server
    return send_file('./static/alert.mp3', mimetype='audio/mpeg')


if __name__ == "__main__":
    app.run(debug=True)
