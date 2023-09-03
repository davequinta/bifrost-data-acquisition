from fastapi import APIRouter
from utils import storage_utils

router = APIRouter()

@router.post("/upload/")
def upload_to_s3(bucket_name: str, file_name: str, data: bytes):
    storage_utils.upload_to_s3(bucket_name, file_name, data)
    return {"status": "success"}
