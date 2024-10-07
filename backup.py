import os
import shutil #coping operation
import datetime
import schedule
import time

source_dir="C:/Users/ronis/OneDrive - Global College of Management/social media"
destination_dir="C:/Users/ronis/OneDrive/backup"


def copy_dir(source,dest):
    today=datetime.date.today()
    dest_dir=os.path.join(dest,str(today))
    print(dest_dir)

    try: 
        shutil.copytree(source,dest_dir)
        print(f"Successfully created a backup folder in {dest_dir}")
    except FileExistsError:
        print(f"backup folder already exist in {dest_dir}")

schedule.every().day.at("22:28").do(lambda: copy_dir(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)

