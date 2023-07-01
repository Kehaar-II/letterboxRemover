from PIL import Image
import sys
import os

import config as cfg

supportedFormats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp"]

def fileExists(filepath):
    if (not os.path.exists(filepath)):
        return False
    if (not os.path.isfile(filepath)):
        return False
    return True

def fileSupported(filepath):
    for format in supportedFormats:
        if (filepath.lower().endswith(format)):
            return 1
    return 0

def saveImage(img, originalPath):
    if (cfg.default["convertToPng"]):
        img = img.save(os.path.splitext(originalPath)[0] + ".png")
        return
    img = img.save(originalPath)
    return

def main():
    filepath = sys.argv[1]

    if (len(sys.argv) < 2):
        print('error: no image was given', file=sys.stderr)
        return 1
    if (not fileExists(filepath)):
        print('error: file doesn\'t exist', file=sys.stderr)
        return 1
    if (not fileSupported(filepath)):
        print('error: file is not an image', file=sys.stderr)
        return 1

    img = Image.open(filepath)

    saveImage(img, filepath)
    return 0

exit(main())
