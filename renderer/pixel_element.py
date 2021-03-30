# import numpy as np
# from renderer.color import *
from component import loggers
from renderer.pixel_renderer import ElementRenderer

logger = loggers.get_logger()


class PixelElement:
    name = ''
    shape = (0, 0)
    position = (0, 0)
    layer = 1
    element_type = 'static'
    element_state = 'before_create'
    element_style = None
    element_renderer = None

    def __init__(self, element_type, color_style=None, element_mask=None, element_style=None):
        if element_type == 'static':
            # Is a static element
            self.element_type = 'static'
            if element_mask is None and color_style is None and element_style:
                logger.error('Need element style parameter.')
                return
            # element style
            if element_style is not None:
                # define element style by element_style
                self.element_style = element_style
            elif element_mask is not None and color_style is not None:
                # define element style by color_style and element mask.
                self.element_style = element_mask * color_style
            else:
                logger.error('Parameters are wrong.')
                return
            self.shape = self.element_style.shape
        elif element_type == 'dynamic':
            # Is a dynamic element
            self.element_type = 'dynamic'
            self.shape = (element_style.shape[1],element_style.shape[2])
            self.element_style = element_style
        else:
            logger.error('Need to assign element_type.')
            return
        # element render
        self.element_renderer = ElementRenderer(self)
