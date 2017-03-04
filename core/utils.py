#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47
import os

from config import *
from core.reader import read_coordinates


def check_static_location_files():
    """
    check the validation of static location files, if the files are missing
    according to the partition settings, create that file
    """
    files = set([f for f in os.listdir(DATA_DIR)])
    checked = set([LOCATION_FILE_NAME+str(i) for i in xrange(X_PARTITION*Y_PARTITION)])

    for c in checked:
        if c not in files:
            f = open(os.path.join(DATA_DIR, c), 'w')
            f.close()


def parse_loc(request, request_type='GET'):
    """
    parse location from http request
    :param request: flask http request
    :param request_type: 'GET' or 'POST'
    :return: parsed lng and lat to [int, int] format. if wrong, return [None, None]
    """

    try:
        if request_type == 'POST':
            lng = int(request.form.get('lng'))
            lat = int(request.form.get('lat'))
        else:
            lng = int(request.args.get('lng'))
            lat = int(request.args.get('lat'))

    except Exception, e:
        # print e
        return [None, None]

    else:
        return [lng, lat]


def coordinate_check(lng, lat):
    """
    check lng and lat
    :param lng: longitude
    :param lat: latitude
    :return: if the two params are both valid
    """

    if lng is None or lat is None:
        return False

    elif type(lng) is not int or type(lat) is not int:
        return False

    elif lng > AXIS_X_MAX or lng < AXIS_X_MIN:
        return False

    elif lat > AXIS_Y_MAX or lat < AXIS_Y_MIN:
        return False

    else:
        return True


def find_nearest(lng, lat, topk=2):
    """
    sort all coordinates in memory and return the nearest k locations
    :param lng: longitude
    :param lat: latitude
    :param topk: top k
    :return: top k nearest locations in a dict with lists
    """

    loc_list = read_coordinates(lng, lat)

    loc_list = sorted(loc_list, key=lambda x: abs(x[0]-lng)+abs(x[1]-lat))

    return {'locations': loc_list[0:topk]}


def get_ipaddr(req):
    """
    :param req: flask request
    :return: host ip of the request
    """
    if req.headers.getlist("X-Forwarded-For"):
        ip = req.headers.getlist("X-Forwarded-For")[0]

    else:
        ip = req.remote_addr

    return ip


# if __name__ == '__main__':
#     print coordinate_check(123, 444)
