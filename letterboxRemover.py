from imports import *

supportedFormats = [".png", ".jpeg", ".jpg", ".ppm", ".gif", ".tiff", ".bmp"]

def fileExists(filepath):
    '''str -> bool \n
    returns True if a file exists, False if it doesn't exist or isn't a file'''
    if (not os.path.exists(filepath)):
        return False
    if (not os.path.isfile(filepath)):
        return False
    return True

def fileSupported(filepath):
    '''str -> bool \n
    returns true if the file is in a format supporet by PIL \n
    the function only checks the file extension of the given filepath'''
    for format in supportedFormats:
        if (filepath.lower().endswith(format)):
            return 1
    return 0

def saveImage(img, originalPath):
    '''Image -> Image \n
    saves the image and converts it to png if the corresponding config value is True'''
    if (default["convertToPng"]):
        img = img.save(os.path.splitext(originalPath)[0] + default["endString"] + ".png")
        return
    img = img.save(os.path.splitext(originalPath)[0] + default["endString"] + os.path.splitext(originalPath)[1])
    return img

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

    croppedImg = cropimage(img, default["blackLevelThreshold"])

    saveImage(croppedImg, filepath)
    return 0

exit(main())
