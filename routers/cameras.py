from fastapi import APIRouter
from utils import rtsp_utils

router = APIRouter()

@router.get("/capture/")
def capture_image(rtsp_url: str):
    image_data = rtsp_utils.capture_image_from_rtsp(rtsp_url)
    return {"status": "success", "image_data": image_data}
