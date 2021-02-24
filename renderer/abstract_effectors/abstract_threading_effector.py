from abc import ABCMeta, abstractmethod
from threading import Thread

from renderer.color import *


class RenderThread(Thread):
    def __init__(self, func, args):
        super(RenderThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


class AbstractThreadingEffector(metaclass=ABCMeta):

    name = 'AbstractThreadingEffector'

    element = None
    position = None
    element_shape = None
    element_style = None

    def __init__(self, element_desc):
        self.element = element_desc['element']
        self.position = element_desc['position']
        self.element_shape = self.element.shape
        self.element_style = self.element.get_element_style()

    def color_transition(self, color_before, color_after, layer_sum, layer_id):
        if color_before == color_after:
            return color_after
        red_before, green_before, blue_before = get_RGB_color(color_before)
        red_after, green_after, blue_after = get_RGB_color(color_after)
        red_step = (red_before - red_after) / layer_sum
        green_step = (green_before - green_after) / layer_sum
        blue_step = (blue_before - blue_after) / layer_sum
        return get_opacity_color(red_before - red_step * layer_id, green_before - green_step * layer_id,
                                 blue_before - blue_step * layer_id)

    def opacity_transition(self, opacity_before, opacity_after, layer_sum, layer_id):
        opacity_step = (opacity_before - opacity_after) / layer_sum
        return int(opacity_before - opacity_step * layer_id)

    def multi_threading_render(self,_func):
        frame_sum = self.get_frame_sum()
        # 线程列表
        threading_list = []
        for frame in range(0,frame_sum):
            thread = RenderThread(_func,args=(frame,frame_sum))
            threading_list.append(thread)
            thread.start()
            thread.join()
        # 初始化一个渲染结果数组
        render_result = np.empty((frame_sum,self.element_shape[0],self.element_shape[1]), dtype='uint32')
        for frame in range(0,frame_sum):
            render_result[frame] = threading_list[frame].get_result()
        return render_result

    # TODO 多线程渲染
    def show_render(self):
        return self.multi_threading_render(self.show)


    def hide_render(self):
        return self.multi_threading_render(self.hide)

    def move_render(self):
        return self.multi_threading_render(self.move)

    def switch_render(self, element_after):
        return self.multi_threading_render(self.switch_render)

    @abstractmethod
    def get_frame_sum(self):
        return 5

    @abstractmethod
    def show(self, frame_id,frame_sum):
        """
        多线程渲染方法，frame_id为帧id
        :param frame_id: 帧id
        :return: 当前过渡帧
        """
        pass

    @abstractmethod
    def hide(self, frame_id,frame_sum):
        """
        多线程渲染方法，frame_id为帧id
        :param frame_id: 帧id
        :return: 当前过渡帧
        """
        pass

    @abstractmethod
    def move(self, frame_id,frame_sum):
        """
        多线程渲染方法，frame_id为帧id
        :param frame_id: 帧id
        :return: 当前过渡帧
        """
        pass

    @abstractmethod
    def switch_element_style(self, element_after, frame_id,frame_sum):
        """
        多线程渲染方法，frame_id为帧id
        :param frame_id: 帧id
        :return: 当前过渡帧
        """
        pass


