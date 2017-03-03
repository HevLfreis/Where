#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 19:09
import os
import random

from config import *


def write_random_locations(filename, length, x_min, x_max, y_min, y_max):
    with open(os.path.join(DATA_DIR, filename), 'w+') as f:
        for _ in xrange(length):
            x, y = random.randint(x_min, x_max), random.randint(y_min, y_max)
            f.write(str(x)+','+str(y)+'\n')

if __name__ == '__main__':
    write_random_locations('loc_part0', 100, -500, 0, 0, 500)
    write_random_locations('loc_part1', 100, -500, 0, -500, 0)
    write_random_locations('loc_part2', 100, 0, 500, 0, 500)
    write_random_locations('loc_part3', 100, 0, 500, -500, 0)
    # print MAP_PARTITION_MATRIX[-400][]
