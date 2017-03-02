#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:56
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

CACHE_BACKEND = 'simple'

AXIS_X_MAX = 500
AXIS_Y_MAX = 500
AXIS_X_MIN = -AXIS_X_MAX
AXIS_Y_MIN = -AXIS_Y_MAX

X_PARTITION = Y_PARTITION = 2

MAP_PARTITION_DICT = {}

BAD_CODE_JSON = {'locations': [None, None]}

LOCATION_FILE_NAME = 'loc_part'

