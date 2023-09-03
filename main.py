#TODO: Add logic to insert data into database 
from fastapi import FastAPI, BackgroundTasks
from utils import rtsp_utils, storage_utils
from datetime import datetime
from time import sleep

app = FastAPI()

RTSP_URL = "rtsp://admin:valhalla%24%242023%23@192.168.1.64:554/Streaming/Channels/101/"

def capture_and_upload():
    while True:
        image_data = rtsp_utils.capture_image_from_rtsp(RTSP_URL)
        file_name = f"snapshot_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        storage_utils.upload_to_s3(file_name, image_data)
        sleep(300)  # Espera 5 minutos

@app.on_event("startup")
def on_startup():
    task = BackgroundTasks()
    task.add_task(capture_and_upload)

@app.get("/")
def read_root():
    return {"message": "Microservicio de Adquisición de Datos"}
