import urllib.request
import pandas as pd
import re
import os


def get_video_id_in_playlist(urls):
    dic = {}
    for page in urls:
        url = urls[page]
        webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=webheader1)
        webPage = urllib.request.urlopen(req)
        contentBytes = webPage.read()
        if page == 'youku':
            contentBytes = re.findall(r'playList.+mod\-pl\-right', str(contentBytes))
            req = urllib.request.Request(url="http://list.youku.com/albumlist/show?id=27312381&ascending=1&page=2", headers=webheader1)
            webPage = urllib.request.urlopen(req)
            contentBytes2 = webPage.read()
            contentBytes2 = re.findall(r'playList.+mod\-pl\-right', str(contentBytes2))
            contentBytes += contentBytes2
            match = r'(<a \S+id\_[^\s]*?\.html)'
            flt = r'id\_(.+?)=='
        elif page == 'youtube':
            contentBytes = re.findall(r'tbody.+tbody', str(contentBytes))
            match = r'(data\-video\-id\=\"[^\s]*?\")'
            flt = r'data\-video\-id\=\"(.+?)\"'
        else:
            raise KeyError
        links = re.findall(match, str(contentBytes))
        all_ids = []
        for link in links:
            find = re.search(flt, link)
            # print(find.group(1))
            all_ids.append(find.group(1))
        print(len(all_ids))
        dic[page+'_id'] = all_ids
    df = pd.DataFrame(dic)
    print(df)
    return df


def assign_to_path(data, path):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        for i, f_name in enumerate(files):
            ids = data.iloc[i, :]
            if ".md" in f_name:
                file_path = root + '/' + f_name
                with open(file_path, 'r') as f:
                    contents = f.readlines()
                    # add content here
                    contents.insert(1, 'youtube_id: %s\n' % ids['youtube_id'])
                    contents.insert(1, 'youku_id: %s\n' % ids['youku_id'])
                with open(file_path, 'w') as f:
                    contents = "".join(contents)
                    f.write(contents)


if __name__ == '__main__':
    # playlist link
    urls = {
        "youku": "http://list.youku.com/albumlist/show?id=27312381&ascending=1&page=1",
        "youtube": 'https://www.youtube.com/playlist?list=PLXO45tsB95cIRP5gCi8AlYwQ1uFO2aQBw'
    }
    path_to_assigned = '_contents/tutorials/python-basic/basic'

    df_ids = get_video_id_in_playlist(urls)
    assign_to_path(df_ids, path=path_to_assigned)