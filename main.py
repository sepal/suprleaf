from time import sleep
from colorsys import hsv_to_rgb
import board
import adafruit_dotstar as dotstar


pixels_per_leaf = 12
num_leafs = 6


num_pixels = pixels_per_leaf * num_leafs
# Might need GRB instead for older DotStar LEDs
order = dotstar.BGR
strip = dotstar.DotStar(board.SCK, board.MOSI, num_pixels,
                        brightness=0.2, auto_write=False, pixel_order=order)

i_leaf = 0
pos = 0.0
while True:
    for leaf in range(0, num_leafs ):
        h = pos+leaf/10
        if h >= 1:
          h = h -1
        color = hsv_to_rgb(h, 0.75, 1)
        color = int(color[0]*255) << 16 | int(color[1]*255) << 8 | int(color[2]*255)
        start_pixel = leaf * pixels_per_leaf
        end_pixel = start_pixel + pixels_per_leaf
        for pixel in range(start_pixel, end_pixel):
            strip[pixel] = color
    strip.show()
    pos += 0.01
    sleep(1.0/50)
