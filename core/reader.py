#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47
from config import *
from core import decorator


def read_coordinates(lng, lat, all_mode=False):
    """
    :param lng: longitude
    :param lat: latitude
    :param all_mode: read all locations mode
    :return: if the request location is located in the partitioned area which
    contains at least one coordinate, return all the coordinates in this area,
    else, return all the coordinates on the map
    """

    scale = float(AXIS_X_MAX-AXIS_X_MIN) / X_PARTITION

    pa = int((lng - AXIS_X_MIN) / scale)
    pb = int((AXIS_Y_MAX - lat) / scale)

    # print MAP_PARTITION_MATRIX[int(pa)][int(pb)]

    loc_list = read_coordinates_from_file(MAP_PARTITION_MATRIX[int(pa)][int(pb)])
    if not loc_list:
        # print 'Read All'
        loc_list = read_coordinates_from_all_files()

    return loc_list


@decorator.get_or_set('location')
def read_coordinates_from_file(part):
    """
    Attention: to accelerate access, the return value will be cached in a cache system
    :param part: the name of the location file
    :return: all coordinates in that file as a list like [[1,2],[3,4]]
    """
    with open(os.path.join(DATA_DIR, part)) as f:
        return [map(int, line.strip().split(',')) for line in f]


def read_coordinates_from_all_files():
    """
    :return: all coordinates on the map
    """
    loc_list = []

    for part in os.listdir(DATA_DIR):
        # print 'part reading: ', part
        with open(os.path.join(DATA_DIR, part)) as f:
            loc_list += [map(int, line.strip().split(',')) for line in f]

    return loc_list
