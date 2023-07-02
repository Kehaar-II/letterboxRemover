I got tired of manually cropping anime screenshots, so instead I wrote this.
# letterboxRemover

letterboxRemover is a simple python program which automatically removes the black bars from the edge of an image.

## Requirements
letterboxRemover requires the followings to work:
- Python 3
- Pillow

## Usage

```bash
$ python3 letterboxRemover.py filepath [-b BLACK_LEVEL_THRESHOLD] [-n OUTPUT_FILEPATH] [-l LEFT_LOWER_LIMIT TOP_LOWER_LIMIT BOTTOM_LOWER_LIMIT RIGHT_LOWER_LIMIT]
```

### Description
<code>-b BLACK_LEVEL_THRESHOLD</code>: highest subpixel value the program considers black <br>
<code>-n OUTPUT_FILEPATH</code>: desired filepath of the output file <br>
<code>-l LEFT_LOWER_LIMIT TOP_LOWER_LIMIT BOTTOM_LOWER_LIMIT RIGHT_LOWER_LIMIT</code>: area that the program will always crop, regardless of color

<br>

written in Python 3.10.11
