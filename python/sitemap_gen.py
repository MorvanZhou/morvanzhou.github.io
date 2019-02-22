
import os
import datetime

os.chdir("/Users/MorvanZhou/Documents/python/morvanzhou.github.io")


lastmod = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).astimezone().isoformat()
sm = ["""<?xml version="1.0" encoding="UTF-8"?>
<urlset
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
    http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        """,
        """
<url>
    <loc>https://morvanzhou.github.io/</loc>
    <lastmod>{0}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
</url>""".format(lastmod),
        "\n</urlset>"
      ]


for root, dirs, files in os.walk("./_site"):
    for f in files:
        if f.endswith(".html"):

            link = root.split('./_site/')[-1]
            if link not in ['./_site', 'static/announcement-files']:
                sublink = root.split('./_site/')[-1] +'/'
                len_sublink = len(sublink.split('/'))
                if len_sublink <= 2:
                    priority = 1.0
                else:
                    priority = 0.8

                sm_temp = """
<url>
    <loc>https://morvanzhou.github.io/{0}</loc>
    <lastmod>{1}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{2}</priority>
</url>""".format(sublink, lastmod, priority)

                sm.insert(-1, sm_temp)


with open('./sitemap.xml', 'w') as sitemap:
    sitemap.writelines(sm)

print("Generate sitemap for %i pages" % (len(sm)-2))