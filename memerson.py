#!/usr/bin/env python
import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def memerson(myimage,caption):
    "memerson(image, sring) -  takes an image and a string caption, and returns a meme"
    draw = ImageDraw.Draw(myimage)
    font = ImageFont.truetype('Arial.ttf', 20)
    textwidth, textheight = draw.textsize(caption, font)
    color = "navy"
    margin = 10
    x = myimage.size[0] - textwidth - margin
    y = myimage.size[1] - textheight - margin

    draw.text((x, y), caption, fill=color, font=font)
    return myimage

if len(sys.argv) != 3:
    print len(sys.argv)
    print memerson.__doc__
else:
    imagefile, caption = sys.argv[1:]
    inputimage = Image.open(imagefile)
    outputimage = memerson(inputimage,caption)
    outputimage.save( 'meme'+caption.strip()+'.png')
