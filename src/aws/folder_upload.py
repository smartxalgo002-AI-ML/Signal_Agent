import boto3
import os

s3 = boto3.client("s3")

bucket_name = "utk-signal-agent"
prefix = "data/"              # S3 folder
local_dir = "data"            # Local folder

# Create local folder if not exists
os.makedirs(local_dir, exist_ok=True)

paginator = s3.get_paginator("list_objects_v2")

for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
    for obj in page.get("Contents", []):
        s3_key = obj["Key"]

        # Skip folder placeholders
        if s3_key.endswith("/"):
            continue

        # Create full local path
        relative_path = os.path.relpath(s3_key, prefix)
        local_path = os.path.join(local_dir, relative_path)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print(f"Downloading {s3_key}...")
        s3.download_file(bucket_name, s3_key, local_path)

print("Download complete ✅")
