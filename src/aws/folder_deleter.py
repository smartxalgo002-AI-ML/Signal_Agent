import shutil
import os

folder_path = "check"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    print("Folder deleted.")
else:
    print("Folder does not exist.")
