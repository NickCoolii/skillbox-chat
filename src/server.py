#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Сервер для обработки сообщений от клиентов
#
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


class ServerProtocol(LineOnlyReceiver):

    def lineReceived(self, line):
        print(f"Message: {line}")


class Server(ServerFactory):

    protocol = ServerProtocol

    def startFactory(self):
        print("Server started")
        # super().startFactory()

reactor.listenTCP(65000, Server())
reactor.run()
