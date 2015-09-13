import socket
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.internet.protocol import DatagramProtocol, Factory
from twisted.protocols.basic import LineReceiver
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.web.static import File


def getIPAddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


client = None


class FrontendHandler(WebSocketServerProtocol):

    def __init__(self):
        global client
        client = self

    def onConnect(self, request):
        print 'Client {} connecting'.format(request.peer)

    def onOpen(self):
        print 'Websocket connection open'

    def onMessage(self, payload, isBinary):
        self.sendMessage(payload, isBinary)
        print 'received message'

    def sendText(self, text):
        self.sendMessage('t' + text, False)

    def sendImage(self, url):
        self.sendMessage('i' + url, False)

    def sendNextSlideCommand(self):
        self.sendMessage('sn', False)

    def sendPrevSlideCommand(self):
        self.sendMessage('sp', False)

    def onClose(self, wasClean, code, reason):
        print 'Websocket connection closed: {}'.format(reason)


class NetworkDiscoveryHandler(DatagramProtocol):

    def startProtocol(self):
        self.transport.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
        self.loopingcall = LoopingCall(self.broadcastService)
        self.loopingcall.start(1)

    def broadcastService(self):
        print 'Broadcasting'
        self.transport.write('Streampoint server {}'.format(getIPAddr()), ('255.255.255.255', 4251))

"""
    def datagramReceived(self, datagram, address):
        if datagram.startsWith('StreamPoint'):
            print 'Device {} pinged me'.format(str(address))
            self.transport.write('StreamPoint server: {}'.format(getIPAddr()), address)
"""


class NetworkDiscoveryMulticastHandler(DatagramProtocol):

    def startProtocol(self):
        self.transport.joinGroup('228.0.0.5')
        self.loopingcall = LoopingCall(self.broadcastService)
        self.loopingcall.start(1)

    def broadcastService(self):
        print 'Broadcasting'
        self.transport.write('Streampoint server {}'.format(getIPAddr()), ('228.0.0.5', 4251))


class RemoteHandler(LineReceiver):

    def __init__(self):
        self.recv = client 

    def lineReceived(self, data):
        d = data.split(' ')
        print data
        cmd = d[0]
        if cmd == 'i':
            if self.recv is not None:
                self.recv.sendImage(d[1])
        elif cmd == 't':
            if self.recv is not None:
                self.recv.sendText(d[1])
        else:
            print 'unknown message {}'.format(data)

    def connectionMade(self):
        peer = self.transport.getPeer()
        print 'Client {0}:{1} connected'.format(peer.host, peer.port)

    def connectionLost(self, reason):
        peer = self.transport.getPeer()
        print 'Client {0}:{1} disconnected'.format(peer.host, peer.port)


if __name__ == '__main__':
    # Network discovery
    protocol = NetworkDiscoveryHandler()
    # reactor.listenUDP(0, protocol)

    """
    protocol = NetworkDiscoveryMulticastHandler()
    reactor.listenMulticast(4251, NetworkDiscoveryMulticastHandler() listenMultiple=True)
    """

    # Websockets
    factory = WebSocketServerFactory('ws://127.0.0.1:4250/socket', debug=True)
    factory.protocol = FrontendHandler
    reactor.listenTCP(4250, factory)

    # Sockets
    factory = Factory()
    factory.protocol = RemoteHandler
    reactor.listenTCP(4252, factory)

    reactor.run()
