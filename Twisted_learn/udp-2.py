#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-12-02 09:03
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import threading
import time
import datetime

host = '127.0.0.1'
port = '8007'


class Echo(DatagramProtocol):

    def startProtocol(self):
        self.transport.connect(host, port)
        self.transport.write(b'here is the first connected message')
        print('connection created')

    def datagramReceived(self, datagram, addr):
        print(datagram.decode('utf8'))

    def connectionRefused(self):
        print('sent failed')

    def stopProtocol(self):
        print('connect closed')


protocol = Echo()


def routine():
    time.sleep(1)
    while True:
        protocol.transport.write(('%s: say hello to myself.' % (datetime.datetime.now())).encode('utf-8'))
        time.sleep(5)


def main():
    threading.Thread(target=routine).start()
    reactor.listenUDP(port, protocol)
    reactor.run()


if __name__ == '__main__':
    main()
