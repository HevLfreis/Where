#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47

from flask import request, abort, jsonify

from config import BAD_CODE_JSON
from core import app
from core.logging import query_logging
from core.utils import coordinate_check, parse_loc, find_nearest


@app.route('/', methods=['GET', 'POST'])
def nearby_location():
    if request.method == 'GET':

        lng, lat = parse_loc(request, 'GET')

        if coordinate_check(lng, lat):
            nr = find_nearest(lng, lat)
            # query_logging(request, [lng, lat], nr)
            return jsonify(nr)

        else:
            # query_logging(request, [lng, lat])
            return jsonify(BAD_CODE_JSON)

    elif request.method == 'POST':

        lng, lat = parse_loc(request, 'POST')

        if coordinate_check(lng, lat):
            nr = find_nearest(lng, lat)
            # query_logging(request, [lng, lat], nr)
            return jsonify(nr)

        else:
            # query_logging(request, [lng, lat])
            return jsonify(BAD_CODE_JSON)

    else:
        abort(403)
