import cv2

def capture_image_from_rtsp(rtsp_url: str) -> bytes:
    cap = cv2.VideoCapture(rtsp_url)
    ret, frame = cap.read()
    if not ret:
        raise Exception("Error capturing image from RTSP")
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()
