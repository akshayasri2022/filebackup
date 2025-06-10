import os
import shutil
import datetime
import schedule
import time

source_dir="C:/Users/COOL/Pictures/Saved Pictures"
destination_dir="C:/Users/COOL/Pictures/Backups"

def copy_folder_to_directory(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))
    
    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in :{dest}")
        
copy_folder_to_directory(source_dir,destination_dir)