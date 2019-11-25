#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-24 10:19
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
