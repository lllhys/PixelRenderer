from abc import ABCMeta, abstractmethod

from renderer.color import *


class AbstractEffector(metaclass=ABCMeta):
    _name_ = 'AbstractEffector'
    _func_ = ['appear', 'disappear', 'move', 'switch']

    element = None
    position = None
    element_shape = None
    element_style = None

    def __init__(self, element):
        self.element = element
        self.position = element.position
        self.element_shape = self.element.shape
        self.element_style = self.element.element_style

    def color_transition(self, color_before, color_after, layer_sum, layer_id):
        if color_before == color_after:
            return color_after
        red_before, green_before, blue_before = get_color_RGB(color_before)
        red_after, green_after, blue_after = get_color_RGB(color_after)
        red_step = (red_before - red_after) / layer_sum
        green_step = (green_before - green_after) / layer_sum
        blue_step = (blue_before - blue_after) / layer_sum
        return get_opacity_color(red_before - red_step * layer_id, green_before - green_step * layer_id,
                                 blue_before - blue_step * layer_id)

    def opacity_transition(self, opacity_before, opacity_after, layer_sum, layer_id):
        opacity_step = (opacity_before - opacity_after) / layer_sum
        return int(opacity_before - opacity_step * layer_id)

    def generate_position_list(self, position, length):
        return [position for i in range(0,length)]

    def appear_render(self):
        return self.appear()

    def disappear_render(self):
        return self.disappear()

    def move_render(self,new_position):
        return self.move(new_position)

    def switch_render(self, element_after):
        return self.switch_element_style(element_after)

    def get_func_by_name(self, effector_name):
        if effector_name == 'appear':
            return self.appear_render
        elif effector_name == 'disappear':
            return self.disappear_render
        elif effector_name == 'move':
            return self.move_render
        elif effector_name == 'switch':
            return self.switch_render
        return None

    @abstractmethod
    def appear(self):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None

    @abstractmethod
    def disappear(self):
        """
        元素过渡动画渲染函数
        :return: 所有过渡帧
        """
        return None

    @abstractmethod
    def move(self,new_position):
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
