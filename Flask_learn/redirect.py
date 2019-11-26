#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-26 09:34
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from flask import abort, redirect, Flask

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/check')

@app.route('/check')
def f_check():
    abort(400)


def main():
    app.run()


if __name__ == '__main__':
    main()
