#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:56
import os
import platform

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

if platform.system() == 'Linux':
    DEPLOYMENT = True
else:
    DEPLOYMENT = False
DEBUG = not DEPLOYMENT

AXIS_X_MAX = 500
AXIS_Y_MAX = 500
AXIS_X_MIN = -AXIS_X_MAX
AXIS_Y_MIN = -AXIS_Y_MAX

X_PARTITION = Y_PARTITION = 2

BAD_CODE_JSON = {'locations': [None, None]}

LOCATION_FILE_NAME = 'loc_part'

MAP_PARTITION_MATRIX = []
config_k = 0
for _ in xrange(X_PARTITION):
    config_a = []
    for __ in xrange(Y_PARTITION):
        config_a.append(LOCATION_FILE_NAME+str(config_k))
        config_k += 1
    MAP_PARTITION_MATRIX.append(config_a)


