#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Библиотека Twisted
#
#  https://twistedmatrix.com/
#  https://pypi.org/project/Twisted/
#
#  Работа с TCP протоколами Twisted, базовой сервер
#
#  1. pip install twisted - установка пакета
#  2. from twisted import ... - подключить в файле .py
#
from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


# если проблема с запуском сервера, то попробуйте сменить порт (1234) на случайный, например 65000
endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
reactor.run()
