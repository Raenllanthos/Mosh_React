import os
import zipfile
from pathlib import Path

# MY SOLUTION 

def main():
    """
    This program makes runnable text. Copy into a command line and it will run.
    You have to be in the root folder for it to work.
    It will go into each folder, find the .mp4, and compress it into a .zip.
    run -- zip.py > (text file name).txt
    This will make a text file. You can then copy paste the code into a command line
    and it will run the necessary steps of git add/commit/push for you.
    
    It is assumed that 'git init' and 'git remote add origin <repo>' has already been completed.
    """

    ROOTPATH = ".\\"
    GITHUB_REPO = "https://github.com/Raenllanthos/Mosh_React.git"
    vids = list(Path(ROOTPATH).rglob("*.[mM][pP][4]"))  
    for vid in vids:
        video = os.path.basename(vid)
        zipName = f"{vid}.zip"
        with zipfile.ZipFile(zipName, "w") as zip:
            zip.write(vid, os.path.basename(vid), zipfile.ZIP_DEFLATED)
            zip.close()
            print(f"git add \"{zipName}\"\
                \ngit commit -m 'added video {video}'\
                \ngit push origin master")

# JON'S SOLUTION
# THIS SOLUTION TAKES THE .mp4 AND PUTS IT ALL INTO IT'S OWN FOLDER
# OF ZIPPED FILES.

    # ROOTPATH = "C:\\Users\\<USERNAME>\\Documents\\"#cullen/desktop
    # SOURCE = "test-dirs"
    # ZIPDIR = "test-zip-git"

    # GITHUB_REPO = "https://github.com/<YOUR USERNAME>/<THE REPO>.git"
    # mode= zipfile.ZIP_STORED
    # print(f"rm -r {os.path.join(ROOTPATH,ZIPDIR)}\
    # \nmkdir {os.path.join(ROOTPATH,ZIPDIR)}\
    # \ncd {os.path.join(ROOTPATH,ZIPDIR)}\
    # \ngit init\
    # \ngit remote add origin {GITHUB_REPO}")

    
    # vids = list(Path(os.path.join(ROOTPATH,SOURCE)).rglob("*.[mM][pP][4]"))
    # for vid in vids:
    #     zipFilePath = vid.__str__().replace(SOURCE, ZIPDIR).replace(".mp4",".zip")

    #     if not os.path.exists(os.path.dirname(zipFilePath)):
    #         os.makedirs(os.path.dirname(zipFilePath))

    #     with zipfile.ZipFile(zipFilePath, 'w') as zip:
    #         zip.write(vid, os.path.basename(vid), mode, 8)
    #         zip.close()
    #         print(f"git add .\
    #         \ngit commit -m 'add vid ${vid}'\
    #         \ngit push origin master")

if __name__ == "__main__":
    main()