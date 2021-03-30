from renderer.abstract_effectors.abstract_effector import AbstractEffector
from renderer.color import *
import numpy as np

class Effector(AbstractEffector):
    _name_ = 'fade'
    _func_ = ['appear', 'disappear', 'move', 'switch']

    frame_sum = 5

    def appear(self):
        # render_layer = np.zeros(self.element_shape, dtype='uint32')
        # it = np.nditer(self.element_style, flags=['multi_index'])
        # while not it.finished:
        #     pixel_color = it[0]
        #     pixel_opacity = get_color_alpha(pixel_color)
        #     if pixel_opacity == 0:
        #         it.iternext()
        #         continue
        #     opacity = self.opacity_transition(0, pixel_opacity, frame_sum, frame_id + 1)
        #     render_layer[it.multi_index[0]][it.multi_index[1]] = set_color_opacity(pixel_color, opacity)
        #     it.iternext()
        render_layer = np.zeros((self.frame_sum,self.element_shape[0],self.element_shape[1]), dtype='uint32')
        for frame in range(0, self.frame_sum):
            for i in range(0, self.element_shape[0]):
                for j in range(0, self.element_shape[1]):
                    pixel_color = self.element_style[i][j]
                    pixel_opacity = get_color_alpha(pixel_color)
                    if pixel_opacity == 0:
                        continue
                    opacity = self.opacity_transition(0, pixel_opacity, self.frame_sum, frame + 1)
                    render_layer[frame][i][j] = set_color_opacity(pixel_color, opacity)
        return self.generate_position_list(self.position, self.frame_sum), render_layer

    def disappear(self):
        # render_layer = np.zeros(self.element_shape, dtype='uint32')
        # # for i in range(0, self.element_shape[0]):
        # #     for j in range(0, self.element_shape[1]):
        # #         pixel_color = self.element_style[i][j]
        # #         pixel_opacity = get_color_opacity(pixel_color)
        # #         if pixel_opacity == 0:
        # #             continue
        # #         opacity = self.opacity_transition(pixel_opacity, 0, frame_sum, frame_id + 1)
        # #         render_layer[i][j] = set_color_opacity(pixel_color, opacity)
        # it = np.nditer(self.element_style, flags=['multi_index'])
        # while not it.finished:
        #     pixel_color = it[0]
        #     pixel_opacity = get_color_alpha(pixel_color)
        #     if pixel_opacity == 0:
        #         it.iternext()
        #         continue
        #     opacity = self.opacity_transition(pixel_opacity, 0, frame_sum, frame_id + 1)
        #     render_layer[it.multi_index[0]][it.multi_index[1]] = set_color_opacity(pixel_color, opacity)
        #     it.iternext()
        # return self.position, render_layer
        render_layer = np.zeros((self.frame_sum,self.element_shape[0],self.element_shape[1]), dtype='uint32')
        for frame in range(0, self.frame_sum):
            for i in range(0, self.element_shape[0]):
                for j in range(0, self.element_shape[1]):
                    pixel_color = self.element_style[i][j]
                    pixel_opacity = get_color_alpha(pixel_color)
                    if pixel_opacity == 0:
                        continue
                    opacity = self.opacity_transition(pixel_opacity, 0, self.frame_sum, frame + 1)
                    render_layer[frame][i][j] = set_color_opacity(pixel_color, opacity)
        return self.generate_position_list(self.position, self.frame_sum), render_layer

    def move(self, new_position):
        hide_pos, hide_result = self.disappear()
        self.element.position = new_position
        self.position = new_position
        show_pos, show_result = self.appear()
        result = np.concatenate((hide_result,show_result),axis=0)
        return hide_pos+show_pos, result

    def switch_element_style(self, element_after):
        # if frame_id < frame_sum / 2:
        #     return self.hide(frame_id, frame_sum / 2)
        # else:
        #     render_layer = np.zeros(self.element_shape, dtype='uint32')
        #     it = np.nditer(self.element_style, flags=['multi_index'])
        #     while not it.finished:
        #         pixel_color = it[0]
        #         pixel_opacity = get_color_alpha(pixel_color)
        #         if pixel_opacity == 0:
        #             it.iternext()
        #             continue
        #         opacity = self.opacity_transition(0, pixel_opacity, frame_sum, frame_id + 1)
        #         render_layer[it.multi_index[0]][it.multi_index[1]] = set_color_opacity(pixel_color, opacity)
        #         it.iternext()
        #     return self.position, render_layer
        pass
