from abc import ABCMeta, abstractmethod
from component import loggers
from renderer.color import *

logger = loggers.get_logger()

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

    def check_result(self, positions, render_result):
        if positions is None or render_result is None:
            logger.warning('The positions or render result is None. '
                           'Please check the results of your effector are correct!')
        if len(positions) == 0 or len(render_result) == 0:
            logger.warning('The length of positions or render result is 0. '
                           'Please check the results of  your effector are correct!')
        if len(positions) is not len(render_result):
            logger.warning('The length of positions is not equal ot the length of render result.')

    def appear_render(self):
        positions, render_result = self.appear()
        self.check_result(positions, render_result)
        return positions, render_result

    def disappear_render(self):
        positions, render_result = self.disappear()
        self.check_result(positions, render_result)
        return positions, render_result

    def move_render(self,new_position):
        positions, render_result = self.move(new_position)
        self.check_result(positions, render_result)
        return positions, render_result

    def switch_render(self, element_after):
        positions, render_result = self.switch_element_style(element_after)
        self.check_result(positions, render_result)
        return positions, render_result

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
        :return: 过渡帧位置，所有过渡帧
        """
        pass


    @abstractmethod
    def disappear(self):
        """
        元素过渡动画渲染函数
        :return: 过渡帧位置，所有过渡帧
        """
        pass

    @abstractmethod
    def move(self,new_position):
        """
        元素过渡动画渲染函数
        :return: 过渡帧位置，所有过渡帧
        """
        pass

    @abstractmethod
    def switch_element_style(self, element_after):
        """
        元素过渡动画渲染函数
        :return: 过渡帧位置，所有过渡帧
        """
        pass
