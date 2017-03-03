#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/9/13
# Time: 13:30
from locust import HttpLocust, TaskSet


def get_nearest(l):
    for i in xrange(-400, 400, 10):
        l.client.get("/?lng="+str(i)+"lat="+str(i))
        l.client.post("/", {"lng": i, "lat": i})


class UserBehavior(TaskSet):
    tasks = {get_nearest: 10}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
