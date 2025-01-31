import os
from dotenv import load_dotenv

load_dotenv()

MINIO_URL = os.getenv('MINIO_URL', 'http://minio:9000')
ACCESS_KEY = os.getenv('ACCESS_KEY', 'minioadmin')
SECRET_KEY = os.getenv('SECRET_KEY', 'minioadmin')
BUCKET_NAME = os.getenv('BUCKET_NAME', 'kafka-data')
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH', "data/raw/")
PREFIX = os.getenv('PREFIX', '')
PROCESSED_PATH = os.getenv('PROCESSED_PATH', '')