import osxphotos

# uses the osxphotos package to query the PHotos library on OSX (Mac)
# https://pypi.org/project/osxphotos/
#
# To Install:
#
#   pip install osxphotos


def interrogateLibrary():
    print('keywords found:')
    print(photosdb.keywords)
    print('persons found:')
    print(photosdb.persons)
    print('albumes found:')
    print(photosdb.albums)


def getFirstVideo():
    videos = photosdb.photos(movies=True)
    firstVideo = videos[0]

    if firstVideo is None:
        return None

    print('First video found is:' + firstVideo.filename)
    print(f'Shot at lat: {firstVideo._latitude} lng: {firstVideo._longitude}')


def main():
    interrogateLibrary()

    getFirstVideo()


photosdb = osxphotos.PhotosDB()
if __name__ == "__main__":
    main()
