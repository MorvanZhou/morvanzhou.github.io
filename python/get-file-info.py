import os
import re
import numpy as np

os.chdir("/Users/MorvanZhou/Documents/python/morvanzhou.github.io")

CATEGORY = 'linux-basic'
SUP_CATEGORY = 'others'

# if find_pattern is None, design the match in below
find_pattern = None  # r'\[.+?\]\(http.+?\)'

res = np.array([], dtype=np.str)
res_cpt = np.array([], dtype=np.int)
titles = []
for root, dirs, filenames in os.walk('./_tutorials/' + SUP_CATEGORY + '/' + CATEGORY):
    for fn in filenames:
        if fn.endswith('.md'):
            with open(os.path.join(root, fn), 'r') as file:
                title = False
                thumbnail = False
                chapter = False
                for line in file.readlines():
                    # replace this match
                    found_title = re.search(r'title:(.+)', line)
                    if found_title:
                        title = found_title.group(1).strip()
                        titles.append(title)

                    found_chapter = re.search(r'chapter:(.+)', line)
                    if found_chapter:
                        chapter = found_chapter.group(1).strip()

                    found_thumbnail = re.search(r'thumbnail:(.+)', line)
                    if found_thumbnail:
                        thumbnail = found_thumbnail.group(1).strip()
                    if title and thumbnail and chapter:
                        break
                if not thumbnail:
                    thumbnail = ""
                res = np.concatenate(
                    (res,
                     np.array(["- [/{0}/{1}, {2}, {3}]\n".format(root[4:], fn[:-3], title, thumbnail)], dtype=np.str)))
                res_cpt = np.concatenate((res_cpt, np.array([chapter])))


results = ''
for i in range(len(os.listdir('./_tutorials/' + SUP_CATEGORY + '/' + CATEGORY))):
    results += "\n{}:\n".format(titles[i])
    same_cpt = res[res_cpt == res_cpt[i]]
    for r in same_cpt:
        if titles[i] not in r:
            results += "  {}".format(r)

path = './_data/recommends/{}.yml'.format(CATEGORY)
if not os.path.isfile(path):
    with open(path, 'w') as file:
        file.write(results)
        print('finish')
else:
    print("File exist! not overwrite!")


