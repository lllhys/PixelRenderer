import random

import numpy as np


def get_hex_color(red, green, blue, white=0):
    return (white << 24) | (red << 16) | (green << 8) | blue


def get_opacity_color(red, green, blue, opacity=0xff):
    return (opacity << 24) | (red << 16) | (green << 8) | blue


def get_RGB_color(hex_color):
    return (hex_color >> 16) & 0x00ff, (hex_color >> 8) & 0x00ff, hex_color & 0x00ff


def get_color_opacity(opacity_color):
    return (opacity_color >> 24) & 0xff


def set_color_opacity(opacity_color, opacity):
    middle = 0x00ffffff & opacity_color
    return (opacity << 24) | middle


def get_random_color_style(shape):
    return np.random.randint(0xff000000,0xffffffff,shape,dtype='uint32')


def get_color_style(shape, color):
    return np.full(shape,color,dtype='uint32')


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
