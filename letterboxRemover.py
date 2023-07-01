from PIL import Image
import sys
import os

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

def main():
    if (len(sys.argv) < 2):
        print('error: no image was given', file=sys.stderr)
        return 1
    if (not fileExists(sys.argv[1])):
        print('error: file doesn\'t exist', file=sys.stderr)
        return 1
    if (not fileSupported(sys.argv[1])):
        print('error: file is not an image', file=sys.stderr)
        return 1

    return 0

exit(main())
