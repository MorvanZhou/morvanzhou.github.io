from selenium import webdriver
import os, re
from bs4 import BeautifulSoup
import time

os.chdir("../")
bili_dir = "python/bili_av_cid"


def scrap():
    os.makedirs(bili_dir, exist_ok=True)
    driver = webdriver.Chrome()     # 打开 Chrome 浏览器

    driver.get("http://space.bilibili.com/243821484/channel/detail?cid=28254")
    input("press enter if page loaded")
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("li", {"class": ["small-item", "fakeDanmu-item"]})

    for item in items:
        try:
            av = item["data-aid"]
        except KeyError:
            continue
        title = item.find_next("a", {"class": "title"}).text
        title = title.replace("/", "_")
        if os.path.exists(os.path.join(bili_dir, title)):
            continue
        f_res = open(os.path.join(bili_dir, title), "w")
        f_res.write("av" + av + "\n")

        base_url = "https://www.bilibili.com/video/av%s/?p=" % av
        i = 0

        while True:
            i+=1
            url = base_url+str(i)
            driver.get(url)
            time.sleep(2)
            html = driver.page_source       # get html

            matched = re.search(r"com/upgcxcode/\d{1,4}/\d{1,4}/(\d{4,12})/", html)
            if matched:
                cid = matched.group(1)
                f_res.write(cid + "\n")
                print(cid)
            else:
                print("NOT FOUND", url)
                break
        f_res.close()
    driver.close()


def switch():
    files = os.listdir(bili_dir)
    av_dict = {}
    for file in files:
        path = os.path.join(bili_dir, file)
        with open(path, "r") as f:
            av_cid = f.readlines()
        av = av_cid[0].strip()
        cids = [c.strip() for c in av_cid[1:]]
        av_dict[av] = cids
    for root, dirs, files in os.walk("_tutorials"):
        if len(files) == 0:
            continue
        files.sort()
        count = 0
        for f in files:
            if f.startswith("."):
                continue
            path = os.path.join(root, f)
            print(path)
            with open(path, "r") as f_data:
                f_str = f_data.read()
            av = re.search(r"bilibili_id:[ ]?(\d{6,8})", f_str)
            if av:
                av = av.group(1)
            else:
                continue
            if path == "_tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch1.md":
                count = 0
            try:
                f_str = re.sub(r"bilibili_id:[ ]?\d{6,8}&page=\d{1,3}\n", "b_av: %s\nb_cid: %s\nb_page: %d\n" % (av, av_dict["av"+av][count], count+1), f_str)
            except KeyError:
                continue
            count += 1
            with open(path, "w") as f_data:
                f_data.write(f_str)


# scrap()
switch()

