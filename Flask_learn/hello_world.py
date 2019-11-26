#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-26 09:19
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    return 'Hello World'


def main():
    app.run()


if __name__ == '__main__':
    main()
