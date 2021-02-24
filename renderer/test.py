import time

from renderer import static_font
from renderer.pixel_canvas import PixelCanvas
from renderer.pixel_element import PixelElement
from renderer.pixel_renderer import Renderer
from renderer.color import *

if __name__ == '__main__':



    pixel_canvas = PixelCanvas((8,32),get_opacity_color(0xff,0,0xff))
    time.sleep(1)


    color_style_1 = get_color_style((5,5),0xffffff00)
    # color_style_1 = get_random_color_style((5,5))
    element_3 = PixelElement(0, static_font.num_3_mask, color_style_1)
    pixel_canvas.put_element('3',element_3,layer=1,position=(1,12))


    color_style_2 = get_color_style((5,5),0xff0000ff)
    # color_style_2 = get_random_color_style((5,5))
    element_5 = PixelElement(0, static_font.num_5_mask, color_style_2)
    pixel_canvas.put_element('5',element_5,layer=2,position=(2,14))
    time.sleep(0.5)


    pixel_canvas.remove_element('5')


    pixel_canvas.show_tool.idle()
