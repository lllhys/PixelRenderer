import time
from renderer import static_font
from renderer.pixel_canvas import PixelCanvas
from renderer.pixel_element import PixelElement
from renderer.color import *

if __name__ == '__main__':
    # 定义一个画布
    pixel_canvas = PixelCanvas((8,32))
    # 停顿1秒
    time.sleep(1)
    # 使用静态资源'数字3'初始化一个元素，颜色为0xff00ff
    element = PixelElement(element_type=3,element_mask=static_font.num_3_mask,color=get_opacity_color(0xff,0,0xff))
    # 将元素放置于画布上
    pixel_canvas.put_element(element_name='3',element=element,layer=1,position=(1,12))
    # 保持窗口停留
    pixel_canvas.show_tool.idle()