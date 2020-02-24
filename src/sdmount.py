import sys

import adafruit_sdcard
import board
import busio
import digitalio
import storage


# Connect to the card and mount the filesystem.
def mount():
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    cs = digitalio.DigitalInOut(board.SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")


# mount()
# sys.path.append("/sd")

