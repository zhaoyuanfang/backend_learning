#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-26 08:55
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        appname = self.get_argument('appname', '')
        if not appname:
            self.write('status')
            return
        self.write('Hello Tornado' + '\t' + appname)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, month, year):
        self.write('日期:%s年%s月' % (year, month))


def make_app():
    return tornado.web.Application([
        (r'/index', MainHandler),
        (r"/index/(?P<year>\d{4})/(?P<month>\d{2})/", IndexHandler),
    ], autoreload=True)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
