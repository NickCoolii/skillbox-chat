#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Графический PyQt 5 клиент для работы с сервером чата
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from gui import design

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver


class ConnectorProtocol(LineOnlyReceiver):
    factory: 'Connector'

    def connectionMade(self):
        # login:admin
        self.factory.window.protocol = self
        self.factory.window.plainTextEdit.appendPlainText("Connected")
        # self.sendLine("login:nick".encode())

    def lineReceived(self, line):
        message = line.decode()
        self.factory.window.plainTextEdit.appendPlainText(message)


class Connector(ClientFactory):
    window: 'ChatWindow'
    protocol = ConnectorProtocol

    def __init__(self, app_window):
        self.window = app_window


class ChatWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    protocol: ConnectorProtocol
    reactor = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self):
        self.pushButton.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        #

    def closeEvent(self, event):
        self.reactor.callFromThread(self.reactor.stop)

    def send_message(self):
        message = self.lineEdit.text()

        if len(message) > 0:
            self.plainTextEdit.appendPlainText('You said: ' + message)
            self.protocol.sendLine(message.encode())
            self.lineEdit.clear()
            self.lineEdit.setFocus()

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
    #         self.send_message()


app = QtWidgets.QApplication(sys.argv)

import qt5reactor

window = ChatWindow()
window.show()

qt5reactor.install()

from twisted.internet import reactor

reactor.connectTCP(
    "localhost",
    65000,
    Connector(window)
)

window.reactor = reactor
reactor.run()
