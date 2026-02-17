import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

aws_access_key_id = os.getenv("GOOGLE_API_KEY")

print(aws_access_key_id)