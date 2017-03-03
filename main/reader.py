#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47
from config import *
from main import decorator


def read_coordinates(lng, lat, all_mode=False):

    scale = float(AXIS_X_MAX-AXIS_X_MIN) / X_PARTITION

    pa = int((lng - AXIS_X_MIN) / scale)
    pb = int((AXIS_Y_MAX - lat) / scale)

    print MAP_PARTITION_MATRIX[int(pa)][int(pb)]

    loc_list = read_coordinates_from_file(MAP_PARTITION_MATRIX[int(pa)][int(pb)])
    if not loc_list:
        print 'Read All'
        loc_list = read_coordinates_from_all_files()

    return loc_list


@decorator.get_or_set('location')
def read_coordinates_from_file(part):
    with open(os.path.join(DATA_DIR, part)) as f:
        return [map(int, line.strip().split(',')) for line in f]


def read_coordinates_from_all_files():
    loc_list = []

    for part in os.listdir(DATA_DIR):
        print 'part reading: ', part
        with open(os.path.join(DATA_DIR, part)) as f:
            loc_list += [map(int, line.strip().split(',')) for line in f]

    return loc_list
