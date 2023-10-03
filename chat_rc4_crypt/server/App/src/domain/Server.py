from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from src.auxiliaries.constants.ServerConstants import *
from src.auxiliaries.utils.ServerUtil import *
from src.domain.services.ServerService import *
from src.domain.ServerUsers import *

class Server:
    def __init__(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((ServerConstants.HOST, ServerConstants.PORT))

        # __name__: Indicates the name of the context in which the python module/file is running
        # In some cases it's done as follows: 'if __name__ == "__main__":'
        if __name__ == "src.domain.Server":
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
