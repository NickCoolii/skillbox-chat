#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Сервер для обработки сообщений от клиентов
#
#  Ctrl + Alt + L - форматирование кода
#
# if user login is restricted - lose connection
# if user login already in use - give another try
# fixed first user massage bug (invisible letters) for Windows default telnet
# anonymous users see no chat messages of users that has login
# if user with login send "die" - he kicks from server with notifying other users
# kick counter for quick senders
# history
# print messages with __debug of ServerProtocol
#
from concurrent.futures.thread import ThreadPoolExecutor
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver
import time


class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None
    __debug = True
    last_message_timestamp: int = 0
    kick_counter: int = 0

    def connectionMade(self):
        self.factory.clients.append(self)
        self.fix_users_first_line_telnet_at_win()

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)

    def lineReceived(self, line: bytes):
        def send_message(user):
            if user is not self and user.login is not None:
                user.sendLine(content.encode())

        # try:
        content = line.decode(errors="ignore")
        # except UnicodeDecodeError:
        #     self.sendLine("Sorry, but I don't understand you. This language/locale is not an option. In English, "
        #                   "please! ".encode())
        #     return

        if self.is_often_messaging():
            self.sendLine("Not so fast. All your base are belong to us…".encode())
            self.check_is_it_tea_time()
            return

        if self.login is not None:
            content = content.strip()
            if len(content) < 1:
                return

            if content.lower() == "die":
                self.transport.loseConnection()
                content = f"{self.login} покидает этот мир."
                with ThreadPoolExecutor(max_workers=20) as pool:
                    pool.map(send_message, self.factory.clients)
                    return

            content = f"{self.login} said: {content}"

            self.factory.update_history(content)
            if self.__debug:
                print(content)

            with ThreadPoolExecutor(max_workers=20) as pool:
                pool.map(send_message, self.factory.clients)

            # for user in self.factory.clients:
            #     if user is not self and user.login is not None:
            #         user.sendLine(content.encode())
        else:
            if self.__debug:
                print(f"Anonymous said '{content}'")
            # login:admin -> admin
            if not content.startswith("login:"):
                self.sendLine("Please, enter your login first like \"login:YOUR_LOGIN_HERE\"".encode())
            else:
                login = content.replace("login:", "")
                login_unique = True

                if login.lower() in self.factory.restricted_logins:
                    self.sendLine("Sorry. Not this time.".encode())
                    self.transport.loseConnection()

                    return
                else:
                    for client in self.factory.clients:
                        if client.login == login:
                            login_unique = False
                            break

                if not login_unique:
                    self.sendLine(f"Логин {login} занят, попробуйте другой".encode())
                else:
                    self.login = login
                    self.sendLine(f"Welcome, {login}! Let's chat! ;)".encode())
                    self.send_history()

                    content = f"{self.login} joined us!"
                    with ThreadPoolExecutor(max_workers=20) as pool:
                        pool.map(send_message, self.factory.clients)
                        return

    def send_history(self):
        if len(self.factory.latest_messages) == 0:
            self.sendLine(f"{self.login}, there is no new messages for ya :|".encode())
        else:
            self.sendLine(b"Here is latest messages:")
            for message in self.factory.latest_messages:
                self.sendLine(message.encode())

    def fix_users_first_line_telnet_at_win(self):
        delimiter = self.delimiter
        self.delimiter = b""
        self.sendLine(">".encode())
        self.delimiter = delimiter

    def is_often_messaging(self):
        previous_message_timestamp = self.last_message_timestamp
        current_message_timestamp = int(time.time())
        self.last_message_timestamp = current_message_timestamp
        return current_message_timestamp - previous_message_timestamp < 1

    def check_is_it_tea_time(self):
        if self.kick_counter > 5:
            self.sendLine(b"Drink some tea and relax. Bye.")
            self.transport.loseConnection()
        else:
            self.kick_counter -= -1


class Server(ServerFactory):
    protocol = ServerProtocol
    clients: list = []
    latest_messages: list = []
    max_count_of_history_messages = 10
    restricted_logins: list = ['admin', 'anonymous']

    def startFactory(self):
        print("Server started")

    def stopFactory(self):
        print("Server closed")

    def update_history(self, message):
        if len(self.latest_messages) >= self.max_count_of_history_messages:
            self.latest_messages.pop(0)

        self.latest_messages.append(message)


reactor.listenTCP(65000, Server())
reactor.run()
