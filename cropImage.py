from imports import *

def isBlack(pixel, threshold):
    '''pixel, int -> bool'''
    for i in range(3):
        if (pixel[i] > threshold):
            return False
    return True

def getLimit(a, b, img, blacklevel):
    '''range, range -> int, int'''

    for i in a:
        for j in b:
            if (not isBlack(img.getpixel((i, j)), blacklevel)):
                return i, j
    return -1, -1

def get_t_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0]
    y = img.size[1]

    i, j = getLimit(range(x), range(default["minCrop"]["top"], y), img, blacklevel)
    if (i == -1):
        return 0
    return max(j, 0)

def get_b_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0]
    y = img.size[1] - default["minCrop"]["bottom"]

    for i in range(x):
        for j in reversed(range(y)):
            if (not isBlack(img.getpixel((i, j)), blacklevel)):
                return min(j, x - 1)
    return x - 1

    # the short form of this one doesn't work and I don't understand why so I'm using the ugly verson here
    # TODO: fix this
    '''
    i, j = getLimit(range(x), reversed(range(y)), img, blacklevel)
    if (i == -1):
        return x - 1
    return min(j, x - 1)
    '''

def get_l_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0]
    y = img.size[1]

    i, j = getLimit(range(default["minCrop"]["left"], x), range(y), img, blacklevel)
    if (i == -1):
        return 0
    return max(i, 0)

def get_r_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0] - default["minCrop"]["right"]
    y = img.size[1]

    i, j = getLimit(reversed(range(x)), range(y), img, blacklevel)
    if (i == -1):
        return x - 1
    return min(i, x - 1)

def cropimage(img, blacklevel):
    '''Imaeg -> Image'''
    cpy = img.copy()
    x = cpy.size[0]
    y = cpy.size[1]
    left = 0
    right = x
    top = 0
    bottom = y

    left = get_l_limit(cpy, blacklevel)
    right = get_r_limit(cpy, blacklevel)
    top = get_t_limit(cpy, blacklevel)
    bottom = get_b_limit(cpy, blacklevel)
    cpy = cpy.crop((left, top, right, bottom))
    return cpy
