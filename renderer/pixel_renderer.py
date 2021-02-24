import time
from renderer.effectors.fade_effector import Effector
from renderer.effector_loader import get_effector
from renderer.color import *



class Renderer:
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

    def diff_handle(self, diff):
        diff_type = diff['diff_type']
        change = diff['change']

        # effector loader 加载效果器
        effector = get_effector(diff['effector_name'])(diff)

        # 变更类型分为状态变更和位置变更
        if diff_type == 'state':
            # 改变类型分为显示和隐藏
            if change == 'show':
                return effector.show_render()
            elif change == 'hide':
                return effector.hide_render()

    def renderer(self):
        diffs = self.canvas.element_diff
        layer_renderer = LayerRenderer(self.canvas)
        time_1 = time.time()
        for diff in diffs:
            print(diff)
            transition_style = self.diff_handle(diff)
            element = diff['element']
            layer_renderer.put_element(diff['position'], diff['layer'], transition_style)
        render_result = layer_renderer.render_layer()
        time_2 = time.time()
        print('renderer time:', time_2 - time_1)
        for i in range(0, render_result.shape[0]):
            time.sleep(0.05)
            self.canvas.show_tool.set_all(render_result[i])
        time_3 = time.time()
        print('show time:', time_3 - time_2)
        # diff 清空
        self.canvas.element_diff.clear()
        # 更新画布最后画面
        self.canvas.canvas_style = layer_renderer.transition_frame[-1]

    def matrix_transition(self, matrix_a, matrix_b, type=0, freq_t=0):
        # logger.info('Matrix transition renderer.')
        # type 1 表示横向过渡
        # type 0 表示纵向过渡
        if type == 1:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=1)  #沿着矩阵行拼接
            matrix = np.hstack((matrix_a, matrix_b))
            # print(matrix.shape)
            while matrix.shape[1] != 32:
                matrix = np.delete(matrix, 0, axis=1)
                # print(matrix.shape)
                self.canvas.show_tool.set_all(matrix)
                time.sleep(freq_t)
        elif type == 0:
            # matrix = np.concatenate((matrix_a,matrix_b),axis=0)  #沿着矩阵行拼接
            matrix = np.vstack((matrix_a, matrix_b))
            # print(matrix.shape)
            while matrix.shape[0] != 8:
                matrix = np.delete(matrix, 0, axis=0)
                # print(matrix.shape)
                self.canvas.show_tool.set_all(matrix)
                time.sleep(freq_t)


class LayerRenderer:
    shape_a = 0
    shape_b = 0
    transition_frame = None
    render_result = None

    def __init__(self, canvas):
        self.shape_a = canvas.shape[0]
        self.shape_b = canvas.shape[1]
        # 层叠渲染最底层样式为当前画布样式
        self.transition_frame = np.empty((1, canvas.layer_sum, self.shape_a, self.shape_b), dtype='uint32')
        self.transition_frame[0] = canvas.canvas_style

    def color_opacity_transition(self, color_before, color_add):
        opaque_value = get_color_opacity(color_add)
        unopacity = (0xff - opaque_value) / 0xff
        opacity = opaque_value / 0xff
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_add, green_add, blue_add = get_RGB_color(color_add)
        red = int(red_before * unopacity + red_add * opacity)
        green = int(green_before * unopacity + green_add * opacity)
        blue = int(blue_before * unopacity + blue_add * opacity)
        return get_hex_color(red, green, blue)

    def same_layer_renderer(self, color_before, color_add):
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_add, green_add, blue_add = get_RGB_color(color_add)
        red = red_before + red_add if red_before + red_add < 256 else 255
        green = green_before + green_add if green_before + green_add < 256 else 255
        blue = blue_before + blue_add if blue_before + blue_add < 256 else 255
        return get_hex_color(red, green, blue)

    def put_element(self, position, layer, transition):
        position_a = position[0]
        position_b = position[1]
        frame_sum = transition.shape[0]

        # 初始化渲染过渡层
        if self.transition_frame.shape[0] < frame_sum:
            for i in range(self.transition_frame.shape[0], frame_sum):
                self.transition_frame = np.insert(self.transition_frame, i, values=self.transition_frame[i - 1], axis=0)
        # 逐帧渲染
        for frame in range(0, frame_sum):
            # 画布层遍历
            for i in range(0, transition.shape[1]):
                for j in range(0, transition.shape[2]):
                    pixel_position_a = position_a + i
                    pixel_position_b = position_b + j
                    # 像素位置合法性判断
                    if pixel_position_a >= self.shape_a or pixel_position_b >= self.shape_b:
                        continue
                    pixel_color = transition[frame][i][j]
                    # print(pixel_color)
                    # 透明度设为0xff时不进行渲染
                    if pixel_color == 0:
                        continue
                    # TODO 同层覆盖时渲染
                    # color_before = self.transition_frame[frame][layer][pixel_position_a][pixel_position_b]
                    # if color_before is not 0:
                    #     # 同层渲染
                    #     color_add = set_color_opacity(pixel_color,128)
                    #     # self.transition_layer[frame + 1][pixel_position_a][pixel_position_b] = self.same_layer_renderer(
                    #     #     color_before, color_add)
                    #     self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] = self.color_opacity_transition(
                    #         color_before, color_add)
                    # else:
                    #     # 样式覆盖
                    #     self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] =  pixel_color
                    self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] = pixel_color

    def render_layer(self):
        self.render_result = np.zeros(
            (self.transition_frame.shape[0], self.transition_frame.shape[2], self.transition_frame.shape[3]),
            dtype='uint32')
        for frame in range(0, self.transition_frame.shape[0]):
            for layer in range(0, self.transition_frame.shape[1]):
                for i in range(0, self.transition_frame.shape[2]):
                    for j in range(0, self.transition_frame.shape[3]):
                        pixel_color = self.transition_frame[frame][layer][i][j]
                        # 不透明度为0
                        if pixel_color < 0x01000000:
                            continue
                        if get_color_opacity(pixel_color) == 0xff or layer == 0:
                            # 完全不透明,清除透明度通道，并赋值
                            self.render_result[frame][i][j] = pixel_color & 0x00ffffff
                        else:
                            # 部分透明
                            color_before = self.render_result[frame][i][j]
                            self.render_result[frame][i][j] = self.color_opacity_transition(color_before, pixel_color)
        return self.render_result
