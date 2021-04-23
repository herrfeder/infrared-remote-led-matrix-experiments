#!/usr/bin/env python
from rgbmatrix import graphics
import random

def set_color(n=1):
    color_list = []
    color_mat = []
    for x in range(0,n):
        for i in range(0,3):
            color_mat.append(random.randint(0,255))
        color_list.append(graphics.Color(color_mat[0], color_mat[1], color_mat[2]))
        color_mat = []    
    return color_list

