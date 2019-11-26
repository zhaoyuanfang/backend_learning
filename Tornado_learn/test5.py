#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-26 08:55
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Tornado')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ], autoreload=True)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
