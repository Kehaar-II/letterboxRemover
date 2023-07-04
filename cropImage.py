from imports import *

def isBlack(pixel):
    '''pixelc -> bool'''
    for i in range(3):
        if (pixel[i] > config["blackLevelThreshold"]):
            return False
    return True

def getLimit(a, b, img):
    '''range, range, Image -> int, int'''

    for i in a:
        for j in b:
            if (not isBlack(img.getpixel((i, j)))):
                return i, j
    return -1, -1

def get_t_limit(img):
    '''Image -> int'''
    x = img.size[0]
    y = img.size[1]

    i, j = getLimit(range(x), range(y), img)
    if (i == -1):
        return 0
    return max(j, 0)

def get_b_limit(img):
    '''Image -> int'''
    x = img.size[0]
    y = img.size[1]

    for i in range(x):
        for j in reversed(range(y)):
            if (not isBlack(img.getpixel((i, j)))):
                return min(j, x - 1)
    return x - 1

    # the short form of this one doesn't work and I don't understand why so I'm using the ugly verson here
    # TODO: fix this
    '''
    i, j = getLimit(range(x), reversed(range(y)), img)
    if (i == -1):
        return x - 1
    return min(j, x - 1)
    '''

def get_l_limit(img):
    '''Image -> int'''
    x = img.size[0]
    y = img.size[1]

    i, j = getLimit(range(x), range(y), img)
    if (i == -1):
        return 0
    return max(i, 0)

def get_r_limit(img):
    '''Image -> int'''
    x = img.size[0]
    y = img.size[1]

    i, j = getLimit(reversed(range(x)), range(y), img)
    if (i == -1):
        return x - 1
    return min(i, x - 1)

def preCrop(img):
    '''Image -> Image'''
    cpy = img.copy()
    x = cpy.size[0]
    y = cpy.size[1]

    cpy = cpy.crop((config["minCrop"]["left"], config["minCrop"]["top"], x - config["minCrop"]["right"], y - config["minCrop"]["bottom"]))
    return cpy

def cropimage(img):
    '''Imaeg -> Image'''
    cpy = preCrop(img)
    x = cpy.size[0]
    y = cpy.size[1]
    left = 0
    right = x
    top = 0
    bottom = y

    left = get_l_limit(cpy)
    right = get_r_limit(cpy)
    top = get_t_limit(cpy)
    bottom = get_b_limit(cpy)
    cpy = cpy.crop((left, top, right, bottom))
    return cpy
