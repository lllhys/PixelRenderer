import numpy as np


def get_hex_color(red, green, blue, white=0):
    """
    获取用于PixelDisplay显示的颜色
    :param red: 红色值
    :param green: 绿色值
    :param blue: 蓝色值
    :param white: 白色值
    :return:
    """
    return (white << 24) | (red << 16) | (green << 8) | blue


def get_opacity_color(red, green, blue, opacity=0xff):
    """
    生成一个具有不透明度的颜色
    :param red: 红色值
    :param green: 绿色值
    :param blue: 蓝色值
    :param opacity: 不透明度
    :return: 不透明度颜色
    """
    return (opacity << 24) | (red << 16) | (green << 8) | blue

def get_opacity_color_from_list(color_list):
    if (color_list[0] == 0) and (color_list[1] == 0) and (color_list[2] == 0):
        return 0x0
    return (0xff << 24) | (color_list[2] << 16) | (color_list[1] << 8) | color_list[0]


def get_color_RGB(hex_color):
    """
    从Hex color 获取RGB通道值
    :param hex_color: hex color
    :return: Red, Green, Blue
    """
    return (hex_color >> 16) & 0x00ff, (hex_color >> 8) & 0x00ff, hex_color & 0x00ff


def get_color_opacity(opacity_color):
    """
    获取颜色不透明度
    :param opacity_color: 不透明度Color
    :return: 不透明度
    """
    return (opacity_color >> 24) & 0xff


def set_color_opacity(opacity_color, opacity):
    """
    设置颜色不透明度
    :param opacity_color: 不透明度Color
    :param opacity: 新的不透明度
    :return: 新的颜色
    """
    middle = 0x00ffffff & opacity_color
    return (opacity << 24) | middle


def get_random_color_style(shape):
    """
    生成用于初始化Element的随机颜色样式
    :param shape: shape样式
    :return: numpy矩阵
    """
    return np.random.randint(0xff000000,0xffffffff,shape,dtype='uint32')


def get_color_style(shape, color):
    """
    生成用于初始化Element的指定颜色样式
    :param shape: shape样式
    :param color: 颜色
    :return: numpy矩阵
    """
    return np.full(shape,color,dtype='uint32')


def color_transition(color_before, color_after, layer_sum, layer_id):
    """
    生成颜色过渡
    :param color_before: 原颜色
    :param color_after: 过渡后颜色
    :param layer_sum: 过渡帧数
    :param layer_id: 当前帧
    :return: 不透明度颜色
    """
    if color_before == color_after:
        return color_after
    red_before, green_before, blue_before = get_color_RGB(color_before)
    red_after, green_after, blue_after = get_color_RGB(color_after)
    red_step = (red_before - red_after) / layer_sum
    green_step = (green_before - green_after) / layer_sum
    blue_step = (blue_before - blue_after) / layer_sum
    return get_opacity_color(red_before - red_step * layer_id, green_before - green_step * layer_id,
                                 blue_before - blue_step * layer_id)

def opacity_transition(opacity_before, opacity_after, layer_sum, layer_id):
    """
    不透明度过渡
    :param opacity_before: 原不透明度
    :param opacity_after: 新不透明度
    :param layer_sum: 过渡帧数
    :param layer_id: 当前帧
    :return: 不透明度
    """
    opacity_step = (opacity_before - opacity_after) / layer_sum
    return int(opacity_before - opacity_step * layer_id)
