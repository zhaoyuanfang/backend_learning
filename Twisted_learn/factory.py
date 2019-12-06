#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time: 2019-11-30 21:42
# @Author: zhaoyuanfang
# @Mail: zhaoyuanfang@datagrand.com
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from protocol import Spreader


class SpreadFactory(Factory):

    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Spreader(self)


def main():
    endpoint = TCP4ServerEndpoint(reactor, 8007),
    endpoint.listen(SpreadFactory())
    reactor.run()


if __name__ == '__main__':
    main()
