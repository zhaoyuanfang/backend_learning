#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-12-01 11:19
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
import sys
import datetime


class Echo(Protocol):

    def connectionMade(self):
        print('connected to the server!')

    def dataReceived(self, data):
        print('got message: ', data.encode('utf8'))
        reactor.callLater(5, self.say_hello)

    def connectionLost(self, reason):
        print('disconnected from the server')

    def say_hello(self):
        if self.transport.connected:
            self.transport.write(
                u"hello, I'm %s %s" % (sys.argv[1], datetime.datetime.now()).encode('utf-8')
            )


class EchoClientFactory(ClientFactory):

    def __init__(self):
        self.protocol = None

    def startedConnecting(self, connector):
        print('started to connect.')

    def buildProtocol(self, addr):
        self.protocol = Echo()
        return self.protocol

    def clientConnectionLost(self, connector, reason):
        print('lost connection, reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('connection failed, reason', reason)


def main():
    host = '127.0.0.1'
    port = 8007
    factory = EchoClientFactory()
    reactor.connectTCP(host, port, factory)
    reactor.run()


if __name__ == '__main__':
    main()
