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

def isJPG(path):
    '''string -> bool'''
    return path.lower().endswith(".jpeg") or path.lower().endswith(".jpg")

def saveImage(img, originalPath, givenPath):
    '''Image, string, string -> Image \n
    saves the image and converts it to png if the corresponding config value is True \n
    if givenPath is non empty the image will be saved to that location in the given format'''
    if (givenPath != ""):
        if (isJPG(givenPath)):
            img = img.convert("RGB")
        img = img.save(givenPath)
        return
    if (default["convertToPng"]):
        if (isJPG(originalPath)):
            img = img.convert("RGB")
        img = img.save(os.path.splitext(originalPath)[0] + default["endString"] + ".png")
        return



    img = img.save(os.path.splitext(originalPath)[0] + default["endString"] + os.path.splitext(originalPath)[1])
    return img

def get_args():
    '''void -> int, string'''

    threshold = default["blackLevelThreshold"]
    name = ""

    for i in range(2, len(sys.argv)):
        if (sys.argv[i] == "-b" and i + 1 < len(sys.argv)):
            threshold = int(sys.argv[i + 1])
        if (sys.argv[i] == "-n" and i + 1 < len(sys.argv)):
            name = sys.argv[i + 1]
    return threshold, name

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
    threshold, name = get_args()

    img = Image.open(filepath)
    croppedImg = cropimage(img, threshold)

    saveImage(croppedImg, filepath, name)
    return 0

exit(main())
