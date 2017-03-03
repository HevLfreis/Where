#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47
import os

from config import *
from main.reader import read_coordinates


def check_static_location_files():
    files = set([f for f in os.listdir(DATA_DIR)])
    checked = set([LOCATION_FILE_NAME+str(i) for i in xrange(X_PARTITION*Y_PARTITION)])

    for c in checked:
        if c not in files:
            f = open(os.path.join(DATA_DIR, c), 'w')
            f.close()


def parse_loc(request, request_type='GET'):

    try:
        if request_type == 'POST':
            lng = int(request.form.get('lng'))
            lat = int(request.form.get('lat'))
        else:
            lng = int(request.args.get('lng'))
            lat = int(request.args.get('lat'))

    except Exception, e:
        print e
        return [None, None]

    else:
        return [lng, lat]


def coordinate_check(lng, lat):
    if lng is None or lat is None:
        return False

    elif type(lng) is not int or type(lat) is not int:
        return False

    elif lng > AXIS_X_MAX or lng < AXIS_X_MIN:
        return False

    elif lat > AXIS_Y_MAX or lng < AXIS_Y_MIN:
        return False

    else:
        return True


def find_nearest(lng, lat, topk=2):

    # Todo: waiting partition
    loc_list = read_coordinates(lng, lat)

    loc_list = sorted(loc_list, key=lambda x: abs(x[0]-lng)+abs(x[1]-lat))

    return {'locations': loc_list[0:topk]}


if __name__ == '__main__':
    print coordinate_check(123, 444)
