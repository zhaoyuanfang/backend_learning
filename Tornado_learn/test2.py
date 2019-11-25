#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-25 09:30
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
import tornado.web
import tornado.ioloop

session_id = 1


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global session_id
        if not self.get_secure_cookie("session"):
            self.set_secure_cookie("session", str(session_id))
            session_id += 1
            self.write("your session got a new session!")
        else:
            self.write("your session was set")


application = tornado.web.Application([
    (r"/", MainHandler),
], cookie_secret='SECRET_DONT_LEAK')


def main():
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
