import re
import time
import argparse
 
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
 
 
def demo(str):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)
    
    print("Created device")
    
    with canvas(device) as draw:
        text(draw, (3,0), str, fill="white", font=proportional(LCD_FONT))
    time.sleep(300)
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
 
    parser.add_argument('--str', type=str, default='hello', help='The string you want to show')
 
    args = parser.parse_args()
 
    try:
        demo(args.str)
    except KeyboardInterrupt:
        pass
