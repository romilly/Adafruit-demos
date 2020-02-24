# The MIT License (MIT)
#
# Copyright (c) 2020 Romilly Cocking
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
runs a slideshow.

The slides should be 320x240 8-bit bitmap files with .bmp as their extension, within a specific directory.

They will be displayed in name order.

Typical usage example:

  loop(directory='/ada/', delay=10)
  bar = foo.FunctionBar()


"""

import board
import displayio
from time import sleep
import os


display = board.DISPLAY


def show(file_path, delay):
    """
    displays a single 320x240 bitmap file.

    :param file_path: the path to the file from the filesystem directory
    :param delay: the length of time in seconds to show the file
    :return:
    """
    with open(file_path, "rb") as bitmap_file:
        bitmap = displayio.OnDiskBitmap(bitmap_file)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=displayio.ColorConverter())
        group = displayio.Group()
        group.append(tile_grid)
        display.show(group)
        sleep(delay)


def list_pix(directory):
    """
    lists the bitmap files in a directory.

    :param directory: the directory to list
    :return: a sorted list of filenames
    """

    return sorted(list([fn for fn in os.listdir(directory) if fn.endswith('.bmp')]))


def loop(directory='/', delay=5):
    """
    repeatedly displays each bitmap file in a directory.

    :param directory:  the directory to search for bitmap files
    :param delay: the length of time in seconds to show the file (default=5)
    :return:
    """
    while True:
        for fn in list_pix(directory):
            show('%s%s' % (directory, fn), delay)

