#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-22 08:54
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.welcome, name='first-url'),
    url(r'moments_input', views.moments_input)
]

def main():
    pass


if __name__ == '__main__':
    main()
