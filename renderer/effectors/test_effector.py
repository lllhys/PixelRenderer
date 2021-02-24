from renderer.abstract_effectors.abstract_threading_effector import AbstractThreadingEffector


class Effector(AbstractThreadingEffector):

    name = 'Test'

    def get_frame_sum(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass

    def move(self):
        pass

    def switch_element_style(self, element_after):
        pass
