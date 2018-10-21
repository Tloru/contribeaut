import datetime
import numpy as np
import cv2
import subprocess
import random
import os

# get the last sunday a year ago
today = datetime.date.today()
year_ago = today.replace(year=(today.year - 1))
idx = (year_ago.weekday() + 1) % 7
sunday_year_ago = year_ago - datetime.timedelta(idx)
date = sunday_year_ago

path = input("Image path (52 by 7): ")
im = cv2.imread(path, 0)[:52][:7].T
print("image size is ", im.shape)

git_folder = input("path to empty git folder: ")

def commit(day, darkness, folder):
    for j in range(int((1 - (darkness / 255)) * 7)):
        filler = str(random.getrandbits(128))
        date = day.strftime(f"%a %d %m %Y 04:20:{69 + j} UTC")

        with open(os.path.join(folder, "x.txt"), "w") as file:
            file.write(filler)

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", filler])
        subprocess.run(["git", "commit", "--amend", "--no-edit", "--date", date])

for week in im:
    for day in week:
        commit(date, day, git_folder)
        date += datetime.timedelta(days=1)

subprocess.run(["git", "push"])
