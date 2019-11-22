#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-22 09:25
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from django.forms import ModelForm
from app.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'


def main():
    pass


if __name__ == '__main__':
    main()
