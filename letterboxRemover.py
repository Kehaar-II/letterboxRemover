from PIL import Image
import sys

if (len(sys.argv) < 2):
    print('error: no image was given', file=sys.stderr)
    exit(1)
