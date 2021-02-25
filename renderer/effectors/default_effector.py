from renderer.abstract_effectors.abstract_effector import AbstractEffector
import numpy as np

class Effector(AbstractEffector):

    _name_ = 'Default'
    _func_ = ['show', 'hide', 'move', 'switch']

    def show(self):

        render_result = np.empty((1,self.element_shape[0],self.element_shape[1]),dtype='uint32')
        render_result[0] = self.element_style
        return [self.position], render_result

    def hide(self):
        render_result = np.zeros((1,self.element_shape[0],self.element_shape[1]),dtype='uint32')
        return [self.position],render_result

    def move(self,new_position):
        frame_sum = abs(self.position[0]-new_position[0])+abs(self.position[1]-new_position[1])
        # render_result = np.empty((frame_sum,self.element_shape[0],self.element_shape[1]),dtype='uint32')
        render_result = np.array([self.element_style]*frame_sum,dtype='uint32')
        position_list = []
        step = 1
        if new_position[0] <self.position[0]:
            step = -1
        for i in range(self.position[0]+step,new_position[0]+step,step):
            position_list.append((i,self.position[1]))
        step = 1
        if new_position[1] <self.position[1]:
            step = -1
        for j in range(self.position[1]+step,new_position[1]+step,step):
            position_list.append((new_position[0],j))
        return position_list,render_result


    def switch_element_style(self, element_after):
        render_result = np.empty((1,element_after.shape[0],element_after.shape[1]),dtype='uint32')
        render_result[0] = element_after.element_style
        return [self.position], render_result

