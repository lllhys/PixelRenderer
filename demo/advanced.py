import time
from renderer import static_font
from renderer.pixel_canvas import PixelCanvas
from renderer.pixel_element import PixelElement
from renderer.color import *

if __name__ == '__main__':
    # 这次我们定义一个红色的画布
    # get_opacity_color是PixelRenderer提供的设置颜色的方法，详见常用api
    pixel_canvas = PixelCanvas((8, 32), get_opacity_color(0xff, 0, 0))
    # 停顿1秒
    time.sleep(1)
    # 使用静态资源'数字3'初始化一个随机颜色的元素
    # get_random_color_style是PixelRenderer提供的产生指定形状大小的随机颜色样式的方法，详见常用api
    element = PixelElement(element_type=1, element_mask=static_font.num_3_mask,
                           color_style=get_random_color_style((5, 5)))
    # 将元素放置于画布上
    pixel_canvas.put_element(element_name='3', element=element, layer=1, position=(1, 12))
    # 停顿一下
    time.sleep(1)
    # 改变一下元素位置
    pixel_canvas.change_element_position(element_name='3', new_position=(2, 15))
    time.sleep(1)
    # 让我们先把自动渲染关闭了，让画面一次有多个改变
    pixel_canvas.auto_renderer_close()
    # 我们把元素'3'删除
    pixel_canvas.remove_element('3')
    # 在元素'3'删除的同时我们再放一个元素上去看看。
    element = PixelElement(element_type=3, element_mask=static_font.num_3_mask, color=get_opacity_color(0, 0, 0xff))
    # 将元素放置于画布上
    pixel_canvas.put_element(element_name='3', element=element, layer=2, position=(1, 12))
    # 让我们打开自动渲染看看效果吧
    pixel_canvas.auto_renderer_open()
    # 保持窗口停留
    pixel_canvas.show_tool.idle()
