import os
import boto3
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm


def download_s3_folder(bucket_name: str, s3_prefix: str, local_dir: str):
    """
    Download an entire folder from S3 to local directory with progress bar.
    """

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

    if not s3_prefix.endswith("/"):
        s3_prefix += "/"

    print(f"Downloading from s3://{bucket_name}/{s3_prefix}")
    print(f"Saving to local folder: {local_dir}\n")

    paginator = s3.get_paginator("list_objects_v2")

    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        for obj in page.get("Contents", []):

            s3_key = obj["Key"]

            if s3_key.endswith("/"):
                continue

            relative_path = s3_key[len(s3_prefix):]
            local_path = os.path.join(local_dir, relative_path)

            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            file_size = obj["Size"]

            print(f"\nDownloading → {relative_path}")

            with tqdm(
                total=file_size,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                desc=relative_path,
            ) as pbar:

                def progress_hook(bytes_amount):
                    pbar.update(bytes_amount)

                s3.download_file(
                    bucket_name,
                    s3_key,
                    local_path,
                    Callback=progress_hook
                )

    print("\nDownload complete ✅")


if __name__ == "__main__":
    download_s3_folder(
        "utk-signal-agent",
        "market_live_rag_data/",
        r"src\aws\check"
    )
