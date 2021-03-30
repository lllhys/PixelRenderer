import numpy as np

from renderer.pixel_renderer import Renderer



class PixelCanvas:

    shape = None
    canvas_style = None
    layer_sum = 4
    elements = {}
    # element_diff = []
    renderer = None
    # auto_renderer = True

    def __init__(self, shape, background=None, layer_sum=4):
        # 画布形状定义
        self.shape = shape
        # 层数定义，默认4层
        self.layer_sum = layer_sum
        # 生成画布样式数组，层数*层shape

        self.canvas_style = np.zeros((layer_sum, shape[0], shape[1]), 'uint32')
        # 设置背景层颜色
        if background is not None:
            self.canvas_style[0] = background
        # 配置渲染器
        self.renderer = Renderer(self)
        # self.render_canvas()

    def put_element(self, element_name, element, layer=1, position=(0, 0), effector_name='default'):
        """
        在画布上放置一个元素
        :param element_name: 元素名
        :param element: 元素对象
        :param layer: 元素所在层
        :param position: 元素位置
        :param effector_name: 效果器名称
        :return: None
        """
        element.name = element_name
        element.position = position
        element.layer = layer
        element.element_state = 'creating'
        if element.element_type == 'dynamic':
            element.element_state = 'show'
        element.element_renderer.change_info['effector'] = effector_name
        self.elements[element_name] = element

    def remove_element(self, element_name, effector_name='default'):
        """
        移除元素
        :param element_name: 元素名
        :param effector_name: 效果器名称
        :return:
        """
        element = self.elements[element_name]
        element.element_state = 'destroying'
        element.element_renderer.change_info['effector'] = effector_name


    def change_element_position(self, element_name, new_position, effector_name='default'):
        """
        改变元素位置
        :param element_name: 元素名
        :param new_position: 新的元素位置
        :param effector_name: 效果器名称
        :return:
        """
        # element_desc = self.elements[element_name]
        # self.element_diff.append({
        #     'element_name': element_name,
        #     'change': 'move',
        #     'effector_name': effector_name,
        #     'layer': element_desc['layer'],
        #     'position': element_desc['position'],
        #     'new_position': new_position,
        #     'element': element_desc['element']})
        # if self.auto_renderer:
        #     self.render_canvas()
        # element_desc['position'] = new_position
        element = self.elements[element_name]
        element.element_state = 'changing'
        # set change info
        element.element_renderer.change_info['effector'] = effector_name
        element.element_renderer.change_info['type'] = 'move'
        element.element_renderer.change_info['new_position'] = new_position



    def switch_element_style(self, element_name, new_style, effector_name='Fade'):
        """
        切换元素样式
        :param element_name: 元素名
        :param new_element: 新的元素样式
        :param effector_name: 效果器名称
        :return:
        """
        # element_desc = self.elements[element_name]
        # self.element_diff.append({
        #     'element_name': element_name,
        #     'change': 'switch',
        #     'effector_name': effector_name,
        #     'layer': element_desc['layer'],
        #     'position': element_desc['position'],
        #     'new_element': new_element,
        #     'element': element_desc['element']})
        # if self.auto_renderer:
        #     self.render_canvas()
        # element_desc['element'] = new_element
        element = self.elements[element_name]
        element.element_state = 'changing'
        # set change info
        element.element_renderer.change_info['effector'] = effector_name
        element.element_renderer.change_info['type'] = 'switch'
        element.element_renderer.change_info['new_position'] = new_style


    def render_canvas(self):
        """
        渲染画布
        :return: None
        """
        # 交由渲染引擎进行差异渲染
        self.renderer.render()

    # def render
