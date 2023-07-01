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

    i, j = getLimit(range(x), range(y), img, blacklevel)
    if (i == -1):
        return 0
    return max(j, 0)

def get_b_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0]
    y = img.size[1]

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

    i, j = getLimit(range(x), range(y), img, blacklevel)
    if (i == -1):
        return 0
    return max(i, 0)

def get_r_limit(img, blacklevel):
    '''Image, int -> int'''
    x = img.size[0]
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
    l_limit = 0
    r_limit = x
    t_limit = 0
    b_limit = y

    l_limit = get_l_limit(cpy, blacklevel)
    r_limit = get_r_limit(cpy, blacklevel)
    t_limit = get_t_limit(cpy, blacklevel)
    b_limit = get_b_limit(cpy, blacklevel)
    cpy = cpy.crop((l_limit, t_limit, r_limit, b_limit))
    return cpy