#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
import sys

inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

img = Image.new("L", (300, 400))
draw = ImageDraw.Draw(img)

font = ImageFont.load("tom-thumb.pil")

texty = 0

for i in range(4):
    draw.text((8, texty), sys.stdin.readline(), inky_display.RED, font)
    texty = (texty + 6)

for line in sys.stdin:
    draw.text((8, texty), line, inky_display.BLACK, font)
    texty = (texty + 6)

inky_display.set_image(img.rotate(90, expand=True))
inky_display.show()
