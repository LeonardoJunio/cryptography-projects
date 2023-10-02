"""Script for Tkinter GUI chat client."""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import RC4
import os

# Adjustment for docker operation, when DISPLAY variable is not found
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

nome = ''
flagNome = True


# nomes de quem entra iguais? gerar nomes aleatorios, com base na data hora (semente)?

class ClientConstants:
    TYPE_CRYPT_RC4 = '1'
    TEXT_PREFIX = "$$$"
    TEXT_ENCODE_SEND = "utf8"
    LEN_MIN_MSG_KEY = 9

    FILE_KEY = "key.txt"

    HOST = '0.0.0.0'
    PORT = 5354
    BUFSIZE = 1024


class ClientUtil:
    @staticmethod
    def convertStrBytes(text: str) -> bytes:
        return bytes(text, ClientConstants.TEXT_ENCODE_SEND)

    def clearInputField(tkMsgStrVar):
        tkMsgStrVar.set("")


class FileUtil:
    def updateKey(key: str):
        FileUtil.writeFile(ClientConstants.FILE_KEY, key)

    def writeFile(filename: str, key: str):
        arquivoChave = open(filename, 'w')
        arquivoChave.write(key)
        arquivoChave.close()


class ClientHelper:
    def handlingIncomingMessages(msg):
        if (msg[0:3] == ClientConstants.TEXT_PREFIX):
            msg = msg.replace('$', "-")
        else:
            msg = RC4.DesencriptarChat(msg)

        return msg

    def processSendedMsg(msg, socketClient, tkTop, nome):
        if (msg == "{quit}"):
            socketClient.send(ClientUtil.convertStrBytes(msg))
            socketClient.close()

            tkTop.quit()

            return

        if (msg[0:7] == "{chave}" and len(msg) > ClientConstants.LEN_MIN_MSG_KEY):
            if (msg[7] == ClientConstants.TYPE_CRYPT_RC4):
                key = msg[8:]

                FileUtil.updateKey(key)

                msg = 'Key modified by ' + nome

                msgEncriptada = RC4.EncriptarChat(msg)
                socketClient.send(ClientUtil.convertStrBytes(msgEncriptada))
            else:
                print("Crypt not defined", flush=True)

            return

        msgEncriptada = RC4.EncriptarChat(msg)
        socketClient.send(ClientUtil.convertStrBytes(msgEncriptada))


class ClientService:
    def receive(socketClient, tkMsgList):
        """Handles receiving of messages."""

        while True:
            try:
                msg = socketClient.recv(BUFSIZE).decode(
                    ClientConstants.TEXT_ENCODE_SEND)

                msg = ClientHelper.handlingIncomingMessages(msg)

                tkMsgList.insert(tkinter.END, msg)
            except OSError:  # Possibly client has left the chat.
                break

    def onReturnSend(tkMsgStrVar, socketClient, tkTop, event=None):
        ClientService.send(tkMsgStrVar, socketClient, tkTop)

    # event is passed by binders.
    def send(tkMsgStrVar, socketClient, tkTop, event=None):
        """Handles sending of messages."""

        msg = tkMsgStrVar.get().strip()

        if not msg:
            ClientUtil.clearInputField(tkMsgStrVar)
            return

        global nome
        if not nome:
            nome = msg
        elif (msg != '{quit}' and msg[0:7] != "{chave}"):
            msg = nome + ': ' + msg

        ClientUtil.clearInputField(tkMsgStrVar)

        ClientHelper.processSendedMsg(msg, socketClient, tkTop, nome)

    def onClosing(tkMsgStrVar, socketClient, tkTop, event=None):
        """This function is to be called when the window is closed."""

        tkMsgStrVar.set("{quit}")
        ClientService.send(tkMsgStrVar, socketClient, tkTop)


tkTop = tkinter.Tk()
tkTop.title("Chat Python")

tkMsgFrame = tkinter.Frame(tkTop)
# For the messages to be sent
tkMsgStrVar = tkinter.StringVar()
# To navigate through past messages
tkScrollbar = tkinter.Scrollbar(tkMsgFrame)
# Following will contain the messages.
tkMsgList = tkinter.Listbox(
    tkMsgFrame,
    height=15,
    width=50,
    yscrollcommand=tkScrollbar.set
)
tkScrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tkMsgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
tkMsgFrame.pack()


tkMsgEntryField = tkinter.Entry(tkTop, textvariable=tkMsgStrVar)
tkMsgEntryField.bind(
    "<Return>",
    lambda event: ClientService.send(tkMsgStrVar, socketClient, tkTop, event)
)
tkMsgEntryField.pack()

# Lambda function creates a temporary simple function to be called
tkSendButton = tkinter.Button(
    tkTop,
    text="Send",
    command=lambda: ClientService.send(tkMsgStrVar, socketClient, tkTop)
)
tkSendButton.pack()

tkTop.protocol(
    "WM_DELETE_WINDOW",
    lambda: ClientService.onClosing(tkMsgStrVar, socketClient, tkTop)
)

HOST = ClientConstants.HOST
PORT = ClientConstants.PORT
BUFSIZE = ClientConstants.BUFSIZE

socketClient = socket(AF_INET, SOCK_STREAM)
socketClient.connect((HOST, PORT))

threadReceive = Thread(
    target=lambda: ClientService.receive(socketClient, tkMsgList))
# A thread that runs in the background, and is not expected to complete its execution before the program exits.
# On the other hand, non-daemon threads are critical to the functioning of the program,
# and they prevent the main program from exiting until they have completed their execution
# The Daemon Thread does not block the main thread from exiting and continues to run in the background.
threadReceive.daemon = True
threadReceive.start()
# Starts GUI execution
tkinter.mainloop()
