#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-12-01 11:34
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import threading
import time
import datetime

host = '127.0.0.1'
port = 8007


class Echo(DatagramProtocol):

    def datagramReceived(self, datagram, addr):
        print('got data from:%s %s' % (addr, datagram.decode('utf8')))


protocol = Echo()


def routine():
    time.sleep(1)
    while True:
        protocol.transport.write(('%s: say hello to myself.' % (datetime.datetime.now())).encode('utf-8'), (host, port))
        time.sleep(5)


def main():
    threading.Thread(target=routine).start()
    reactor.listenUDP(port, protocol)
    reactor.run()


if __name__ == '__main__':
    main()
