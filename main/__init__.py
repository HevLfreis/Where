#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:48
from flask import Flask, request
from flask.ext.cache import Cache

from config import CACHE_BACKEND

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': CACHE_BACKEND})

# Todo: add redis cache
# cache = Cache(app, config={
#     'CACHE_TYPE': 'redis',
#     'CACHE_KEY_PREFIX': 'where',
#     'CACHE_REDIS_HOST': 'localhost',
#     'CACHE_REDIS_PORT': '6379',
#     'CACHE_REDIS_URL': 'redis://localhost:6379'
#     })

from routes import *