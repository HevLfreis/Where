#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2016/9/13
# Time: 13:30
from locust import HttpLocust, TaskSet


def get_nearest(l):
    l.client.post("/login/", {"a": "b"})


class UserBehavior(TaskSet):
    tasks = {get_nearest: 10}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
