import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

# Force load .env from project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")

print("KEY:", aws_access_key_id)
print("REGION:", region_name)

if not aws_access_key_id or not aws_secret_access_key:
    raise ValueError("AWS credentials not loaded. Check your .env file.")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

bucket_name = "utk-signal-agent"
local_folder = "src/market_live_rag/data"
s3_prefix = "data/"

for root, dirs, files in os.walk(local_folder):
    for file in files:
        local_path = os.path.join(root, file)

        relative_path = os.path.relpath(local_path, local_folder)
        s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

        print(f"Uploading {local_path} to {s3_path}")
        s3.upload_file(local_path, bucket_name, s3_path)

print("Upload complete ✅")
