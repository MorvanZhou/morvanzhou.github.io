import os
import re

def search_replace(path, old=r'{% link .* %}', new='#'):
    if os.path.isfile(path):
        f_name = path.split('/')[-1]
        if ".md" in f_name:
            file_path = path
            with open(file_path, 'r') as file:
                filedata = file.read()
                matches = re.findall(old, filedata)
                print(matches)
            for matched in matches:
                filedata = filedata.replace(matched, new)
            with open(file_path, 'w') as file:
                file.write(filedata)
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        for f_name in files:
            if ".md" in f_name:
                file_path = root+'/'+f_name
                with open(file_path, 'r') as file:
                    filedata = file.read()
                    matches = re.findall(old, filedata)
                    print(matches)
                for matched in matches:
                    filedata = filedata.replace(matched, new)
                with open(file_path, 'w') as file:
                    file.write(filedata)

if __name__ == "__main__":
    search_replace(
        '_contents/tutorials/data-manipulation/plt/',
        old=r'youtube_id:.*',
        new=''
    )