from threading import Thread

from src.auxiliaries.constants.ServerConstants import *
from src.auxiliaries.utils.ServerUtil import *

class ServerService:
    def acceptIncomingConnections(server, clients, addresses):
        """Sets up handling for incoming clients."""

        while True:
            client, client_address = server.accept()

            client.send(ServerUtil.convertStrBytes(ServerConstants.USER_NAME))

            addresses[client] = client_address

            Thread(
                target=ServerService.handleClient,
                args=(clients, client)
            ).start()

    def handleClient(clients, client):
        """Handles a single client connection. Takes client socket as argument."""

        # Need to stay before sending the broadcast
        nameClient = client.recv(ServerConstants.BUFSIZE).decode("utf8")

        ServerService.broadcast(clients,
                                ServerUtil.convertStrBytes(ServerConstants.USER_ENTER_ALL))

        client.send(ServerUtil.convertStrBytes(ServerConstants.USER_ENTER))

        clients[client] = nameClient

        while True:
            msgClient = client.recv(ServerConstants.BUFSIZE)

            # Prevents the user from manipulating whether or not to generate encryption
            if msgClient[0:3] == ServerConstants.TEXT_PREFIX:
                msgClient = msgClient.replace('$', "")

            if msgClient != ServerUtil.convertStrBytes("{quit}", False):
                ServerService.broadcast(clients, msgClient)
            else:
                msgClient = ServerUtil.convertStrBytes(
                    ServerConstants.USER_LEFT)

                client.send(ServerUtil.convertStrBytes("{quit}"))
                client.close()
                del clients[client]

                ServerService.broadcast(clients, msgClient)

                break

    def broadcast(clients, msg):
        """Broadcasts a message to all the clients."""

        for sock in clients:
            sock.send(msg)
            