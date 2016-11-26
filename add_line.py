import os

def add_line(path):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        for i, f_name in enumerate(files):
            if ".md" in f_name:
                file_path = root+'/'+f_name
                with open(file_path, 'r') as f:
                    contents = f.readlines()
                    # add content here
                    contents.insert(1, 'index: %s\n' % str(i+1))
                with open(file_path, 'w') as f:
                    contents = "".join(contents)
                    f.write(contents)

add_line('_contents/tutorials/machine-learning/test')