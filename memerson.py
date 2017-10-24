#!/usr/bin/env python
import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def old_skool(pngimage):  
    for x in range(pngimage.size[0]):
        for y in range(pngimage.size[1]):
            (r, g, b) = pngimage.getpixel((x,y))[:3]
            alpha = pngimage.getpixel((x,y))[3:]
            pngimage.putpixel((x, y), ( r - 122 , g + 122, b - 122 ) + alpha)
    
def memerson(myimage,caption):
    """./memerson image, string -  takes an image and a string caption, and returns a meme.\n
    additional arguments will run a filter before creating a meme
    e.g. ./memerson.py "balloons.png' 'hello'
    or ./memerson.py "balloons.png' 'hello' 'old_skool'
    """
    draw = ImageDraw.Draw(myimage)
    font = ImageFont.truetype('Arial.ttf', 20)
    textwidth, textheight = draw.textsize(caption, font)
    color = "navy"
    margin = 10
    x = myimage.size[0] - textwidth - margin
    y = myimage.size[1] - textheight - margin

    draw.text((x, y), caption, fill=color, font=font)
    return myimage

if len(sys.argv) <= 2:
    print len(sys.argv)
    print memerson.__doc__
else:
    imagefile, caption = sys.argv[1:3]
    inputimage = Image.open(imagefile)
    if sys.argv[3]=='old_skool':
        input = old_skool(inputimage)
    else:
        print 'No filter named '+sys.argv[3]
    outputimage = memerson(inputimage,caption)
    outputimage.save( 'M_'+caption.strip()+'.png')
