import numpy as np

from renderer.pixel_renderer import Renderer
from tools.pixel_display import PixelDisplay




class PixelCanvas:
    show_tool = PixelDisplay(pixel_size=25)
    shape = None
    canvas_style = None
    layer_sum = 4
    elements = {}
    element_diff = []
    renderer = None
    auto_renderer = True

    def __init__(self, shape, background=0x0,layer_sum=4):
        # 画布形状定义
        self.shape = shape
        # 层数定义，默认4层
        self.layer_sum = layer_sum
        # 生成画布样式数组，层数*层shape

        self.canvas_style = np.zeros((layer_sum,shape[0], shape[1]), 'uint32')
        # 设置背景层颜色
        if background is not 0x0:
            print(np.__version__)
            self.canvas_style[0] = np.full(shape,fill_value=background,dtype='uint32')
            # self.canvas_style[0] = np.array([[background] * shape[1]] * shape[0], 'uint32')
        # 配置渲染器
        self.renderer = Renderer(self)
        self.render_canvas()



    def put_element(self, element_name, element, layer=1, position=(0, 0), effector_name='Fade'):
        self.elements[element_name] = {'layer': layer, 'position': position, 'element': element}
        self.element_diff.append({
            'element_name': element_name,
            'diff_type': 'state',
            'change': 'show',
            'effector_name': effector_name,
            'layer': layer,
            'position': position,
            'element': element})
        if self.auto_renderer:
            self.render_canvas()

    def remove_element(self, element_name, effector_name='Fade'):
        element_desc = self.elements[element_name]
        self.element_diff.append({
            'element_name': element_name,
            'diff_type': 'state',
            'change': 'hide',
            'effector_name': effector_name,
            'layer': element_desc['layer'],
            'position': element_desc['position'],
            'element': element_desc['element']})
        self.elements.pop(element_name)
        if self.auto_renderer:
            self.render_canvas()

    def change_element_level(self, element_name, level):
        self.elements.get(element_name).update('level', level)

    def change_element_position(self, element_name,position,effector_name='Default'):
        element_desc = self.elements[element_name]
        element_desc['position'] = position
        self.element_diff.append({
            'element_name': element_name,
            'diff_type': 'state',
            'change': 'move',
            'effector_name': effector_name,
            'layer': element_desc['layer'],
            'position': element_desc['position'],
            'element': element_desc['element']})



    def render_canvas(self):
        '''
        渲染
        :return:
        '''
        # 交由渲染引擎进行差异渲染
        self.renderer.renderer()

    def show(self):
        # print(self.matrix)
        self.render_canvas()
        # self.show_tool.set_all(self.canvas_style)


    def auto_renderer_open(self):
        '''
        打开自动渲染，并进行渲染
        :return: None
        '''
        self.auto_renderer = True
        self.render_canvas()

    def auto_renderer_close(self):
        '''
        关闭自动渲染
        :return: None
        '''
        self.auto_renderer = False

    def auto_renderer_switch(self):
        '''
        切换自动渲染状态
        :return: None
        '''
        if self.auto_renderer:
            self.auto_renderer_close()
        else:
            self.auto_renderer_open()


