from renderer.abstract_effectors.abstract_effector import AbstractEffector
import numpy as np

class Effector(AbstractEffector):

    name = 'Default'

    def show(self):
        render_result = np.empty((1,self.element_shape[0],self.element_shape[1]),dtype='uint32')
        render_result[0] = self.element_style
        return render_result

    def hide(self):
        render_result = np.zeros((1,self.element_shape[0],self.element_shape[1]),dtype='uint32')
        return render_result

    def move(self):
        pass

    def switch_element_style(self, element_after):
        pass

