import boto3
import os
from dotenv import load_dotenv
from pathlib import Path
from tqdm import tqdm

# Load .env
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")

if not aws_access_key_id or not aws_secret_access_key:
    raise ValueError("AWS credentials not loaded. Check your .env file.")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

bucket_name = "utk-signal-agent"
local_folder = BASE_DIR / "src\market_live_rag\data"
s3_prefix = "market_live_rag_data/"

print("Starting upload...\n")

class ProgressPercentage:
    def __init__(self, filename):
        self._filename = filename
        self._size = os.path.getsize(filename)
        self._pbar = tqdm(total=self._size, unit='B', unit_scale=True)

    def __call__(self, bytes_amount):
        self._pbar.update(bytes_amount)

for root, dirs, files in os.walk(local_folder):
    for file in files:

        if file.startswith("."):
            continue

        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_folder)
        s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

        print(f"\nUploading → {s3_path}")

        s3.upload_file(
            local_path,
            bucket_name,
            s3_path,
            Callback=ProgressPercentage(local_path)
        )

print("\nUpload complete ✅")
