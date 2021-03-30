import time
from renderer.effectors.fade_effector import Effector
from renderer.effector_loader import get_effector
from renderer.color import *
import cv2

class Renderer:
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas




    def render(self):
        layer_renderer = LayerRenderer(self.canvas)
        destroyed_list = []
        for element_item in self.canvas.elements.items():
            element = element_item[1]
            # render the element
            render_result = element.element_renderer.render()
            layer_renderer.render_layer(element,render_result)
            # destroy the element witch state is destroyed
            if element.element_state == 'destroyed':
                destroyed_list.append(element_item[0])
        # destroy the element witch state is destroyed
        for item in destroyed_list:
            self.canvas.elements.pop(item)
        render_result = layer_renderer.render_canvas()
        return render_result



        # diffs = self.canvas.element_diff
        #
        # time_1 = time.time()
        # for diff in diffs:
        #     # print(diff)
        #     transition_position, transition_style = self.diff_handle(diff)
        #     layer_renderer.render_layer(diff, transition_position, transition_style)
        # render_result = layer_renderer.render_canvas()
        # time_2 = time.time()
        # print('renderer time:', time_2 - time_1)
        # for i in range(0, render_result.shape[0]):
        #     time.sleep(0.05)
        #     self.canvas.show_tool.set_all(render_result[i])
        # # time_3 = time.time()
        # # print('show time:', time_3 - time_2)
        # # diff 清空
        # self.canvas.element_diff.clear()
        # # 更新画布最后画面
        # self.canvas.canvas_style = layer_renderer.transition_frame[-1]

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


    def show_from_numpy(self, img_np):
        # print(img_np.shape)
        # 图片数组裁剪
        canvas_rate = self.canvas.shape[1]/self.canvas.shape[0]
        img_rate = img_np.shape[1] / img_np.shape[0]
        result = np.zeros(self.canvas.shape,dtype="uint32")
        if canvas_rate>img_rate:
            block_size = int(img_np.shape[1] / result.shape[1])
            base = int((img_np.shape[0] - block_size * result.shape[0]) / 2)
            # width 重合，裁剪height
            for i in range(0,result.shape[0]):
                for j in range(0,result.shape[1]):
                    block = img_np[base + block_size * i:base + block_size * (i + 1), block_size * j:block_size * (j + 1)]
                    blue= int(np.mean(block[:,:,0:1]))
                    green = int(np.mean(block[:,:,1:2]))
                    red = int(np.mean(block[:,:,2:]))
                    result[i][j] = get_hex_color(red,green,blue)
        else:
            block_size = int(img_np.shape[0] / result.shape[0])
            base = int((img_np.shape[1] - block_size * result.shape[1]) / 2)
            # width 重合，裁剪height
            for i in range(0,result.shape[0]):
                for j in range(0,result.shape[1]):
                    block = img_np[block_size * i:block_size * (i + 1), base + block_size * j:base + block_size * (j + 1)]
                    blue= int(np.mean(block[:,:,0:1]))
                    green = int(np.mean(block[:,:,1:2]))
                    red = int(np.mean(block[:,:,2:]))
                    result[i][j] = get_hex_color(red,green,blue)
        return result

    def show_from_picture(self,picture):
        img = cv2.imread(picture)
        result = self.show_from_numpy(img)
        self.canvas.show_tool.set_all(result)

    def show_from_video(self,video,loop_repeat):
        while True:
            cap = cv2.VideoCapture(video)#打开视频
            while cap.isOpened():
                ret,frame = cap.read() #读取视频返回视频是否结束的bool值和每一帧的图像
                if not ret:
                    break
                result = self.show_from_numpy(frame)
                self.canvas.show_tool.set_all(result)
            if loop_repeat is not True:
                break


class ElementRenderer:
    element = None
    current_frame = 0
    change_info = {'effector': 'default', 'type': 'move'}
    render_tmp = None
    position_tmp = None

    def __init__(self, element):
        self.element = element

    def show(self):
        if self.element.element_type == 'static':
            return self.element.element_style
        else:
            result = self.element.element_style[self.current_frame]
            self.current_frame = self.current_frame+1
            if self.current_frame >= self.element.element_style.shape[0]:
                self.current_frame = 0
            return result

    def render_frame(self, type, *args):
        if self.current_frame == 0:
            # do render if is the first time.
            effector = get_effector(self.change_info['effector'], type)(self.element)
            self.position_tmp, self.render_tmp = effector.get_func_by_name(type)(*args)
        # return current frame
        render_type = False
        frame = self.render_tmp[self.current_frame]
        self.element.position = self.position_tmp[self.current_frame]
        # update current_frame
        self.current_frame = self.current_frame+1
        if self.current_frame == self.render_tmp.shape[0]:
            self.current_frame = 0
            render_type = True
            # clear the temp
            self.render_tmp = None
        return render_type, frame


    def appear(self):
        return self.render_frame('appear')

    def disappear(self):
        return self.render_frame('disappear')

    def move(self):
        return self.render_frame('move', self.change_info['new_position'])

    def switch_style(self):
        # TODO
        return self.render_frame('switch', self.change_info['new_style'])


    def update_element_state(self,render_type):
        if render_type == True:
            if self.element.element_state == 'destroying':
                self.element.element_state = 'destroyed'
            else:
                self.element.element_state = 'show'


    def render(self):
        render_type = False
        result = None
        if self.element.element_state == 'creating':
            render_type, result = self.appear()
        elif self.element.element_state == 'destroying':
            render_type, result = self.disappear()
        elif self.element.element_state == 'changing':
            if self.change_info['type'] == 'move':
                render_type, result = self.move()
            elif self.change_info['type'] == 'switch':
                render_type, result = self.switch_style()
        else:
            # show state
            return self.show()
        # update element state
        self.update_element_state(render_type)
        return result


class LayerRenderer:
    shape = (0, 0)
    transition_frame = None
    render_result = None

    def __init__(self, canvas):
        self.shape = canvas.shape
        # 层叠渲染第一帧样式为当前画布背景层
        self.transition_frame = np.zeros((canvas.layer_sum, self.shape[0], self.shape[1]), dtype='uint32')
        self.transition_frame[0] = canvas.canvas_style[0]

    def color_opacity_transition(self, color_before, color_add):
        opaque_value = get_color_alpha(color_add)
        unopacity = (0xff - opaque_value) / 0xff
        opacity = opaque_value / 0xff
        red_before, green_before, blue_before = get_color_RGB(color_before)
        red_add, green_add, blue_add = get_color_RGB(color_add)
        red = int(red_before * unopacity + red_add * opacity)
        green = int(green_before * unopacity + green_add * opacity)
        blue = int(blue_before * unopacity + blue_add * opacity)
        return get_hex_color(red, green, blue)

    # def same_layer_renderer(self, color_before, color_add):
    #     red_before, green_before, blue_before = get_color_RGB(color_before)
    #     red_add, green_add, blue_add = get_color_RGB(color_add)
    #     red = red_before + red_add if red_before + red_add < 256 else 255
    #     green = green_before + green_add if green_before + green_add < 256 else 255
    #     blue = blue_before + blue_add if blue_before + blue_add < 256 else 255
    #     return get_hex_color(red, green, blue)

    # def clear_element(self, layer, position, element, canvas):
    #     for i in range(0, element.shape[0]):
    #         for j in range(0, element.shape[1]):
    #             if element.element_mask[i][j] == 0:
    #                 continue
    #             canvas[layer][position[0] + i][position[1] + j] = 0
    #     return canvas



    def render_layer(self, element, transition):
        # layer = diff['layer']
        # # self.clear_element(layer, diff['position'], diff['element'], self.transition_frame[0])
        # frame_sum = transition.shape[0]
        #
        # # 初始化渲染过渡层
        # if self.transition_frame.shape[0] < frame_sum:
        #     for i in range(self.transition_frame.shape[0], frame_sum):
        #         self.transition_frame = np.insert(self.transition_frame, i, values=self.transition_frame[i - 1], axis=0)
        # # 逐帧渲染
        # for frame in range(0, frame_sum):
        #     position_a = transition_position[frame][0]
        #     position_b = transition_position[frame][1]
        #     # 画布层遍历
        #     for i in range(0, transition.shape[1]):
        #         for j in range(0, transition.shape[2]):
        #             pixel_position_a = position_a + i
        #             pixel_position_b = position_b + j
        #             # 像素位置合法性判断
        #             if pixel_position_a >= self.shape_a or pixel_position_b >= self.shape_b or pixel_position_a<0 or pixel_position_b < 0:
        #                 continue
        #             pixel_color = transition[frame][i][j]
        #             # print(pixel_color)
        #             # 透明度设为0xff时不进行渲染
        #             # if pixel_color == 0:
        #             #     continue
        #             # TODO 同层覆盖时渲染
        #             # color_before = self.transition_frame[frame][layer][pixel_position_a][pixel_position_b]
        #             # if color_before is not 0:
        #             #     # 同层渲染
        #             #     color_add = set_color_opacity(pixel_color,128)
        #             #     # self.transition_layer[frame + 1][pixel_position_a][pixel_position_b] = self.same_layer_renderer(
        #             #     #     color_before, color_add)
        #             #     self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] = self.color_opacity_transition(
        #             #         color_before, color_add)
        #             # else:
        #             #     # 样式覆盖
        #             #     self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] =  pixel_color
        #             self.transition_frame[frame][layer][pixel_position_a][pixel_position_b] = pixel_color

        it = np.nditer(transition, flags=['multi_index'])
        while not it.finished:
            pixel_color = it[0]
            # check whether transparency is equal to 0
            if pixel_color < 0x01000000:
                it.iternext()
                continue
            pixel_position_a = it.multi_index[0]+element.position[0]
            pixel_position_b = it.multi_index[1]+element.position[1]
            # 像素位置合法性判断
            if pixel_position_a >= self.shape[0] or pixel_position_b >= self.shape[1] or pixel_position_a<0 or pixel_position_b < 0:
                it.iternext()
                continue
            self.transition_frame[element.layer][pixel_position_a][pixel_position_b] = pixel_color
            it.iternext()

    def render_canvas(self):
        self.render_result = np.zeros(self.shape, dtype='uint32')
        # 新版本 使用nditer
        it = np.nditer(self.transition_frame, flags=['multi_index'])
        while not it.finished:
            pixel_color = it[0]
            # 不透明度为0
            if pixel_color < 0x01000000:
                it.iternext()
                continue
            target_index = (it.multi_index[1],it.multi_index[2])
            # 0层不需要渲染，以及不透明不需要渲染
            if it.multi_index[0] == 0 or get_color_alpha(pixel_color) == 0xff:
                # 完全不透明,清除透明度通道，并赋值
                self.render_result.itemset(target_index,pixel_color & 0x00ffffff)
                # self.render_result[index[0]][index[1]][index[2]] = pixel_color & 0x00ffffff
            else:
                # 部分透明
                color_before = self.render_result.item(target_index)
                self.render_result.itemset(target_index, self.color_opacity_transition(color_before, pixel_color))
                # self.render_result[index[0]][index[1]][index[2]] = self.color_opacity_transition(color_before, pixel_color)
            it.iternext()
        return self.render_result
