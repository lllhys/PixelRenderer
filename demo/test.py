import os
import time

from renderer import static_font
from renderer.pixel_canvas import PixelCanvas
from renderer.pixel_element import PixelElement
from renderer.pixel_renderer import Renderer
from renderer.color import *

if __name__ == '__main__':


# ,get_opacity_color(0xff,0,0xff)
    pixel_canvas = PixelCanvas((8,32),background=0x0,layer_sum=4)
    time.sleep(1)
    # color_style_1 = get_random_color_style((6,6))
    # element_p = PixelElement(0,element_mask=static_font.P_mask,color_style=color_style_1)
    # pixel_canvas.put_element('p',element_p,1,(1,10))
    # pixel_canvas.auto_renderer_close()
    # pixel_canvas.auto_renderer_open()
    color_style_1 = get_random_color_style((5,5))
    element_3 = PixelElement(element_type=3,element_mask=static_font.num_3_mask,color=get_opacity_color(0xff,0,0xff))
    pixel_canvas.put_element(element_name='3',element=element_3,layer=1,position=(1,12))


    color_style_2 = get_color_style((5,5),0xffffff00)
    # color_style_2 = get_random_color_style((5,5))
    element_5 = PixelElement(0, color_style_2, static_font.num_5_mask)
    pixel_canvas.put_element('5',element_5,layer=2,position=(3,14))

    # pixel_canvas.auto_renderer_open()
    time.sleep(0.5)

    pixel_canvas.auto_renderer_close()
    pixel_canvas.change_element_position('3',(3,14))

    pixel_canvas.change_element_position('5',(-1,12))

    pixel_canvas.auto_renderer_open()
    time.sleep(0.5)
    # pixel_canvas.remove_element('5')
    # pixel_canvas.remove_element('3')
    new_element = PixelElement(1, color_style_2, static_font.num_5_mask)
    pixel_canvas.switch_element_style(element_name='5',new_element=new_element)

    # pixel_canvas.remove_element('5')
    pixel_canvas.change_element_position('5',(4,4))
    pixel_canvas.put_element('5',element_5,3,(0,13))

    pixel_canvas.show_tool.idle()



