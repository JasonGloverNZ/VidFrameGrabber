import photos

#print(dir (photos))

# help(photos)


def show_photo(index=-1):

    all_assets = photos.get_assets()
    last_asset = all_assets[index]
    img = last_asset.get_image()
    img.show()

    print(len(all_assets))


def show_frame(index, frame):

    videos = photos.get_assets(media_type='video')
    video = videos[index]
    print(video.local_id)
    print(dir(video))
    print(video.duration)
    print(video.location)
    print(video.get_image_data())
    get_video = video.get_image()

    print(dir(video.get_image))
    # help(video)
    # help(video.get_image())

    # video.seek(frame)
    get_video.show()
    #get_video2 = video.get_image().seek(1)

    # get_video2.show()

    get_video2 = video.seek(frame)

    get_video2.show()
    print(len(videos))

# help(video.get_image())

# show_photo(100)


show_frame(-100, 20)

# https://github.com/tdamdouni/Pythonista/blob/master/video/quicklook-video.py


# https://forum.omz-software.com/topic/482/how-to-save-image-via-photos-save_image

"""
import Image
import photos
from urllib import urlopen
from io import BytesIO

print "Downloading image..."
url = "http://omz-software.com/pythonista/docs/_static/pythonista_icon.png"
img = Image.open(BytesIO(urlopen(url).read()))
photos.save_image(img)
print "Image saved to camera roll."

"""
