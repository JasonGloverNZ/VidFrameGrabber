import cv2
import os
import argparse

#
# Exports every frame of the video as a jpg.
#
# USAGE:
#
# --v parameter specifies path to the video
# --o parameter specifies path (directory) to export the frames.
#
# python3 extractImages.py --v MiniVanMadness.mov --o frames_output
#


def extractImages(pathToVideo, pathToOutput):

    pathToVideo = "MiniVanMadness.mov" if pathToVideo is None else pathToVideo
    pathToOutput = "frames_output" if pathToOutput is None else pathToOutput

    # Read the video from specified path
    cam = cv2.VideoCapture(pathToVideo)

    try:
        # creating a folder named data
        if not os.path.exists(pathToOutput):
            os.makedirs(pathToOutput)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0

    while (True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './' + pathToOutput + '/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--v", help="path to video")
    a.add_argument("--o", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.v, args.o)
