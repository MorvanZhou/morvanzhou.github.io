from PIL import Image
import os

os.chdir("/Users/MorvanZhou/Documents/python/morvanzhou.github.io")


def change_size(job_name='thumbnails'):
    jobs = {"thumbnails":
                {'source': './static/thumbnail', 'target': './static/thumbnail-small'},
            'course-covers':
                {'source': './static/img/course_cover', 'target': './static/img/course_cover-small'}
            }

    # select job
    job = jobs[job_name]

    source = job['source']
    target = job['target']
    basewidth = 300

    for root, dirs, filenames in os.walk(source):
        path = os.path.join(target, root.split('/')[-1] if root.replace("/", "") != source.replace("/", "") else "")
        if not os.path.isdir(path):
            os.mkdir(path)
        for fn in filenames:
            extension = fn.split('.')[-1].lower()
            if extension in ['jpg', 'png', 'jpeg']:
                save_path = os.path.join(path, fn)
                if not os.path.isfile(save_path):
                    img = Image.open(os.path.join(root, fn))
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                    img.save(save_path)
                    print(save_path)


def reduce_icon(to_height=64):
    for name in os.listdir('./static/img/icon'):
        if name.split('.')[-1].lower() in ['jpg', 'png']:
            im = Image.open("./static/img/icon/%s" % name)
            w, h = im.size
            h_ = h / to_height
            w /= h_
            im = im.resize((int(w), to_height), Image.ANTIALIAS)
            im.save("./static/img/icon/%s" % name)


def reduce_single(path, to_height=256):
    im = Image.open(path)
    w, h = im.size
    h_ = h / to_height
    w /= h_
    im = im.resize((int(w), to_height), Image.ANTIALIAS)
    im.save(path)


if __name__ == "__main__":
    job_name = ['thumbnails', 'course-covers'][1]
    change_size(job_name)
    # reduce_icon()
    # reduce_single(path='static/img/description/more_update.png', to_height=130)

