import numpy as np


class PixelElement:
    shape = (0,0)
    element_mask = None
    color_style = None
    element_style = None

    def __init__(self, element_type, color_style=None, element_mask=None):
        if element_type == 0:
            if element_mask is None or color_style is None:
                # logger.error('element type设为掩膜+颜色时，element_mask或color_matrix不允许为空')
                print('element type设为掩膜+颜色时，element_mask或color_matrix不允许为空')
                return
            self.element_mask = element_mask
            self.color_style = color_style
            self.element_style = self.get_element_style()
            self.shape = element_mask.shape
        elif element_type == 1:
            if color_style is None:
                # logger.error('element type设为仅颜色时，color_matrix不允许为空')
                print('element type设为仅颜色时，color_matrix不允许为空')
                # return
            self.color_style = color_style
            self.element_style = color_style
            self.shape = color_style.shape
            self.element_mask = np.ones(self.shape,dtype='uint8')
        else:
            # logger.error('非法的element_type')
            print('非法的element_type')


    def get_element_style(self):
        if self.element_mask is None:
            return self.color_style
        else:
            return self.element_mask*self.color_style
