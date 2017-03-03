#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/2
# Time: 16:48
from flask import Flask, request
from flask.ext.cache import Cache

from config import DEPLOYMENT

app = Flask(__name__)

if not DEPLOYMENT:
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})
else:
    cache = Cache(app, config={
        'CACHE_TYPE': 'redis',
        'CACHE_KEY_PREFIX': 'where',
        'CACHE_REDIS_HOST': 'localhost',
        'CACHE_REDIS_PORT': '6379',
        'CACHE_REDIS_URL': 'redis://localhost:6379/2'
        })

from routes import *