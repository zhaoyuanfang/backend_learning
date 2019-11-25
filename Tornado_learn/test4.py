#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-25 21:20
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define, options, parse_command_line

clients = dict()


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("index.html")


class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args):
        self.id = self.get_argument('Id')
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}

    def on_message(self, message):
        print(("Client %s received a message: %s" % (self.id, message)))

    def on_close(self):
        if self.id in clients:
            del clients[self.id]
            print("Client %s is closed" % (self.id))

    def check_origin(self, origin):
        return

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/websocket', MyWebSocketHandler),
])

import threading
import time
import datetime
import asyncio


def send_time():
    asyncio.set_event_loop(asyncio.new_event_loop())
    while True:
        for key in clients.keys():
            msg = str(datetime.datetime.now())
            clients[key]['object'].write_message(msg)
            print("write to client %s: %s" % (key, msg))
        time.sleep(1)


def main():
    threading.Thread(target=send_time).start()
    parse_command_line()
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
