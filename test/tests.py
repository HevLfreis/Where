#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 19:09
import os
import random

from config import *


def write_random_locations(filename, length):
    with open(os.path.join(DATA_DIR, filename), 'w+') as f:
        for _ in xrange(length):
            x, y = random.randint(AXIS_X_MIN, AXIS_X_MAX), random.randint(AXIS_Y_MIN, AXIS_Y_MAX)
            f.write(str(x)+','+str(y)+'\n')

if __name__ == '__main__':
    write_random_locations('loc_part1', 100)
    # print MAP_PARTITION_MATRIX[-400][]
