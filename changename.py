import os

def change(path):

    for root, dirs, files in os.walk(path):
        for f_name in files:
            if f_name[1] == ".":
                new_name = f_name.replace('.', '-', 1)
                print(new_name)
                os.rename(path+f_name, path+new_name)

if __name__ == "__main__":
    change("_tutorial_page_contents/")