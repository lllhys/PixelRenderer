import time
from tkinter import *
import random

class PixelDisplay():

    shape = (8,32)

    def __init__(self,shape=(8,32),pixel_size=20):
        self.shape = shape
        # 建立一个框架对象tk
        self.tk = Tk(className='PixelDisplay')
        # 建立一个画布对象canvas，属于tk对象
        self.canvas = Canvas(self.tk, width=shape[1]*pixel_size, height=shape[0]*pixel_size)
        # 将画布对象更新显示在框架中
        self.canvas.pack()
        # 初始化像素矩阵
        self.rectangle_list = []
        for i in range(0, shape[0]):
            line_list = []
            for j in range(0, shape[1]):
                re = self.canvas.create_rectangle(j * pixel_size, i * pixel_size, (j + 1) * pixel_size, (i + 1) * pixel_size, outline='white',
                                                  fill='black')
                line_list.append(re)
            self.rectangle_list.append(line_list)



    def get_hex_color(self, color):
        '''
        颜色转换
        :param color: 32bit color
        :return: TK color
        '''
        # return '#%02x%02x%02x'%(color[0],color[1],color[2])
        return '#%06x' % color

    def set_one(self, position, color):
        '''
        设置某一像素颜色
        :param position: tuple 像素位置
        :param color: 32bit color
        :return: None
        '''
        self.canvas.itemconfig(self.rectangle_list[position[0]][position[1]], fill=self.get_hex_color(color))
        self.tk.update()

    def set_all_same(self, color):
        '''
        将所有像素设置为同一颜色
        :param color: 32bit color
        :return: None
        '''
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill=self.get_hex_color(color))
        self.tk.update()

    def set_all(self,color_matrix):
        '''
        将所有像素按color matrix设置
        :param color_matrix: 颜色矩阵
        :return: None
        '''
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill=self.get_hex_color(color_matrix[i][j]))
        self.tk.update()
    def clear_one(self, position):
        '''
        清除某一像素颜色
        :param position: tuple 像素位置
        :return: None
        '''
        self.canvas.itemconfig(self.rectangle_list[position[0]][position[1]], fill='black')
        self.tk.update()

    def clear_all(self):
        '''
        清除所有像素
        :return: None
        '''
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                self.canvas.itemconfig(self.rectangle_list[i][j], fill='black')
        self.tk.update()

    def idle(self):
        self.canvas.mainloop()
