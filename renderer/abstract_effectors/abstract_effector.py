from abc import ABCMeta, abstractmethod

from renderer.color import *


class AbstractEffector(metaclass=ABCMeta):

    name = 'AbstractEffector'

    element = None
    position = None
    element_shape = None
    element_style = None

    def __init__(self, element_desc):
        self.element = element_desc['element']
        self.position = element_desc['position']
        self.element_shape = self.element.shape
        self.element_style = self.element.get_element_style()

    def color_transition(self, color_before, color_after, layer_sum, layer_id):
        if color_before == color_after:
            return color_after
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_after, green_after, blue_after = get_RGB_color(color_after)
        red_step = (red_before - red_after) / layer_sum
        green_step = (green_before - green_after) / layer_sum
        blue_step = (blue_before - blue_after) / layer_sum
        return get_opacity_color(red_before - red_step * layer_id, green_before - green_step * layer_id,
                                 blue_before - blue_step * layer_id)

    def opacity_transition(self, opacity_before, opacity_after, layer_sum, layer_id):
        opacity_step = (opacity_before - opacity_after) / layer_sum
        return int(opacity_before - opacity_step * layer_id)

    def show_render(self):
        return self.show()

    def hide_render(self):
        return self.hide()

    def move_render(self):
        return self.move()

    def switch_render(self,element_after):
        return self.switch_element_style(element_after)


    @abstractmethod
    def show(self):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None

    @abstractmethod
    def hide(self):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None

    @abstractmethod
    def move(self):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None

    @abstractmethod
    def switch_element_style(self, element_after):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None




