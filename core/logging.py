#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/3/3
# Time: 10:44
import datetime
from pymongo import MongoClient

# mongo for logging
from core.utils import get_ipaddr

client = MongoClient()
db = client.where


def query_logging(request, loc, rep=None):
    context = {'host': get_ipaddr(request),
               'source': loc,
               'timestamp': datetime.datetime.now()}
    if rep is not None:
        context.update(rep)
    # print context
    db.logs.insert_one(context)
