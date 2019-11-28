#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-27 09:24
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def f_root(): pass


@app.route('/industry')
def f_industry(): pass


@app.route('/book/<book_name>')
def f_book(book_name): pass


with app.test_request_context():
    print(url_for('f_root'))
    print(url_for('f_industry'))
    print(url_for('f_industry', name='web'))
    print(url_for('f_book', book_name='Python Book'))


def main():
    pass


if __name__ == '__main__':
    main()
