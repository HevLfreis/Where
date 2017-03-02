#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:47

from flask import request, abort, jsonify

from config import BAD_CODE_JSON
from main import app
from main.utils import coordinate_check, parse_loc, find_nearest


@app.route('/', methods=['GET', 'POST'])
def nearby_location():
    if request.method == 'GET':

        lng, lat = parse_loc(request, 'GET')

        if coordinate_check(lng, lat):
            return jsonify(find_nearest(lng, lat))

        else:
            return jsonify(BAD_CODE_JSON)

    elif request.method == 'POST':

        lng, lat = parse_loc(request, 'POST')

        if coordinate_check(lng, lat):
            return jsonify(find_nearest(lng, lat))

        else:
            return jsonify(BAD_CODE_JSON)

    else:
        abort(403)
