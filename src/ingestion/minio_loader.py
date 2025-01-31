from minio import Minio
import config
import os


print(config.MINIO_URL)

client = Minio(
    config.MINIO_URL.replace("http://", "").replace("https://", ""),
    access_key=config.ACCESS_KEY,
    secret_key=config.SECRET_KEY,
    secure=False,
)

def list_bucket_files(prefix):
    objects = client.list_objects(config.BUCKET_NAME, prefix=prefix)
    return [obj.object_name for obj in objects]


def download_files():
    """ Baixa todos os arquivos do bucket MinIO """
    os.makedirs(config.DOWNLOAD_PATH, exist_ok=True)
    files = list_bucket_files(config.PREFIX)

    for file in files:
        local_path = os.path.join(config.DOWNLOAD_PATH, file)
        client.fget_object(config.BUCKET_NAME, file, local_path)
        print(f"Baixado: {file} → {local_path}")


