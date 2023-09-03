import boto3

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

BUCKET_NAME = "bifrost-bucket"


def upload_to_s3(file_name: str, data: bytes):
    s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=data)
