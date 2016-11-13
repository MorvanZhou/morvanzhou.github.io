import os
import re

def search_replace(path, old=r'{% link .* %}', new='#'):
    for root, dirs, files in os.walk(path):
        print(files)
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
    # change("_tutorial_page_contents/")
    search_replace(
        '_contents/tutorials/machine-learning/ML-intro',
        old=r']\(#\)',
        new=']({% link %})'
    )