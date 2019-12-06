#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-30 21:34
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from twisted.internet.protocol import Protocol

clients = []


class Spreader(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMase(self):
        self.factory.numProtocols += 1
        self.transport.write(
            (u'welcome to spred site, u r the %d 位 user!\n') % (self.factory.numProtocols)).encode('utf8')
        clients.append(self)

    def connectionsLost(self, reason):
        clients.remove(self)
        print('lost connect: %d' % self.connect_id)

    def dataReceived(self, data):
        if data == 'close':
            self.transport.loseConnection()
            print("%s closed" % self.connect_id)
        else:
            print('spreding message from %s: %s' % (self.connect_id, data))
            for client in clients:
                if client != self:
                    client.transport.write(data)


def main():
    pass


if __name__ == '__main__':
    main()
