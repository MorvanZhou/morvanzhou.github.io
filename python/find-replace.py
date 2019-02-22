import os
import re

os.chdir("/Users/MorvanZhou/Documents/python/morvanzhou.github.io")
source = './_tutorials'

# if find_pattern is None, design the match in below
find_pattern = None  # r'\[.+?\]\(http.+?\)'


test = input("test[Y/n]")
if test.lower() == 'n':
    test = False
    conform = input("Have committed changes?[y/N]")
    if conform.lower() != 'y':
        exit()
else:
    test = True

for root, dirs, filenames in os.walk(source):
    for fn in filenames:
        if fn.endswith('.md'):
            file_replaced = False
            with open(os.path.join(root, fn), 'r') as file:
                new_contents = []
                for line in file.readlines():
                    # replace this match
                    match = r'<img.+?src="/static/results/rl/(.+?)".+?>' if find_pattern is None else find_pattern
                    found = re.search(match, line)
                    if found:
                        file_replaced = True
                        print('\nreplace for %s' % file.name)
                        # replace this line
                        line = re.sub(find_pattern, '{0}{{:target="_blank"}}'.format(found.group()), line)
                    new_contents.append(line)

                new_contents = ''.join(new_contents)

            if test and file_replaced:
                print(new_contents)

            if not test:
                with open(os.path.join(root, fn), 'w') as file:
                    file.write(new_contents)

print('finish')