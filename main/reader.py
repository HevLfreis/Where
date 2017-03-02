#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47
from config import *


def read_coordinates(lng, lat):

    a = (lng - AXIS_X_MIN) / (AXIS_X_MAX-AXIS_X_MIN)
    b = (lat - AXIS_Y_MIN) / (AXIS_Y_MAX-AXIS_Y_MIN)
    print a, b


    with open(DATA_DIR+'/loc_part1') as f:
        return [map(int, line.strip().split(',')) for line in f]
