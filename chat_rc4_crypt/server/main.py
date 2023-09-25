"""
Server for multithreaded (asynchronous) chat application.
It needs to be started first
"""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class ServerUsers:
    clients = {}
    addresses = {}


class ServerConstants:
    TEXT_PREFIX = "$$$"
    TEXT_ENCODE_SEND = "utf8"

    HOST = ''
    PORT = 5354
    # No of bytes to receive
    BUFSIZE = 1024

    USER_NAME = "Type your name, please."
    USER_ENTER_ALL = "User entered the chat."
    USER_ENTER = "Welcome to the chat."
    USER_LEFT = "User left the chat."


class ServerUtil:
    @staticmethod
    def convertStrBytes(text: str, prefix: bool = True) -> bytes:
        if (prefix):
            text = ServerConstants.TEXT_PREFIX + text

        return bytes(text, ServerConstants.TEXT_ENCODE_SEND)


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


class Server:
    def init(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((ServerConstants.HOST, ServerConstants.PORT))

        # __name__: Indicates the name of the context in which the python module/file is running
        if __name__ == "__main__":
            # Show the print on docker compose
            # This will cause the entire buffer to flush, not just the same print call.
            # So if there are 'bare' print function calls elsewhere (i.e. without flush=True)
            # that weren't explicitly unbuffered, these will always be flushed too.
            print("Waiting for connection...", flush=True)

            serverUsers = ServerUsers()
            clients = serverUsers.clients
            addresses = serverUsers.addresses

            # Queue size through the parameter backlog. This denotes maximum number
            # of connections that can be queued for this socket by the operating system
            server.listen(5)

            acceptThread = Thread(
                target=ServerService.acceptIncomingConnections,
                args=(server, clients, addresses)
            )
            acceptThread.start()
            acceptThread.join()

        server.close()


Server().init()
