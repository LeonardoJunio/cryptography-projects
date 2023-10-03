"""Script for Tkinter GUI chat client."""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from datetime import datetime, timezone, timedelta
import tkinter
import RC4
import os

# Adjustment for docker operation, when DISPLAY variable is not found
if os.environ.get('DISPLAY', '') == '':
    # print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


class User:
    name = ''


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


class DateTimeUtil:
    def setTimeZoneBrasil():
        return timezone(timedelta(hours=-3))

    @staticmethod
    def getDateTimeNowBrasil():
        timeZone = DateTimeUtil.setTimeZoneBrasil()
        return datetime.now().astimezone(timeZone)

    @staticmethod
    def getDateTimeNowFormat():
        dtNow = DateTimeUtil.getDateTimeNowBrasil()
        return dtNow.strftime("%d/%m/%Y %H:%M:%S")

    @staticmethod
    def getTimeNowFormat():
        dtNow = DateTimeUtil.getDateTimeNowBrasil()
        return dtNow.strftime("%H:%M:%S")

    @staticmethod
    def getTimeNowBrackets() -> str:
        timeNowFormat = DateTimeUtil.getTimeNowFormat()
        return "[" + timeNowFormat + "] "


class ClientHelper:
    def handlingIncomingMessages(msg):
        if (msg[0:3] == ClientConstants.TEXT_PREFIX):
            return msg.replace('$', "-")
        
        return RC4.DesencriptarChat(msg)

    def processSendedMsg(msgInput, socketClient, tkTop, user):
        timeNow = DateTimeUtil.getTimeNowBrackets()

        if (msgInput == "{quit}"):
            socketClient.send(ClientUtil.convertStrBytes(msgInput))
            socketClient.close()

            tkTop.quit()

            return

        if (msgInput[0:7] == "{chave}" and len(msgInput) > ClientConstants.LEN_MIN_MSG_KEY):
            if (msgInput[7] == ClientConstants.TYPE_CRYPT_RC4):
                key = msgInput[8:]

                FileUtil.updateKey(key)

                msgInput = timeNow + 'Key modified by ' + user.name

                msgEncrypted = RC4.EncriptarChat(msgInput)
                socketClient.send(ClientUtil.convertStrBytes(msgEncrypted))
            else:
                print("Crypt not defined", flush=True)

            return

        msgEncrypted = RC4.EncriptarChat(timeNow + msgInput)
        socketClient.send(ClientUtil.convertStrBytes(msgEncrypted))


class ClientService:
    def receive(socketClient, tkMsgList):
        """Handles receiving of messages."""

        while True:
            try:
                msgRecv = socketClient.recv(ClientConstants.BUFSIZE).decode(
                    ClientConstants.TEXT_ENCODE_SEND)

                msgRecv = ClientHelper.handlingIncomingMessages(msgRecv)

                tkMsgList.insert(tkinter.END, msgRecv)
            except OSError:  # Possibly client has left the chat.
                break

    # Event is passed by binders.
    def send(user, tkMsgStrVar, socketClient, tkTop, event=None):
        """Handles sending of messages."""

        msgInput = tkMsgStrVar.get().strip()

        if not msgInput:
            ClientUtil.clearInputField(tkMsgStrVar)
            return

        if not user.name:
            user.name = msgInput
        elif (msgInput != '{quit}' and msgInput[0:7] != "{chave}"):
            msgInput = user.name + ': ' + msgInput

        ClientUtil.clearInputField(tkMsgStrVar)

        ClientHelper.processSendedMsg(msgInput, socketClient, tkTop, user)

    def onClosing(user, tkMsgStrVar, socketClient, tkTop, event=None):
        """This function is to be called when the window is closed."""

        tkMsgStrVar.set("{quit}")
        ClientService.send(user, tkMsgStrVar, socketClient, tkTop)


class Client:
    def init(self):
        user = User()

        tkTop = tkinter.Tk()
        tkTop.title("Chat (Python)")

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
            lambda event: ClientService.send(
                user, tkMsgStrVar, socketClient, tkTop, event)
        )
        tkMsgEntryField.pack()

        # Lambda function creates a temporary simple function to be called
        tkSendButton = tkinter.Button(
            tkTop,
            text="Send",
            command=lambda: ClientService.send(
                user, tkMsgStrVar, socketClient, tkTop)
        )
        tkSendButton.pack()

        tkTop.protocol(
            "WM_DELETE_WINDOW",
            lambda: ClientService.onClosing(
                user, tkMsgStrVar, socketClient, tkTop)
        )

        socketClient = socket(AF_INET, SOCK_STREAM)
        socketClient.connect((ClientConstants.HOST, ClientConstants.PORT))

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


# nomes de quem entra iguais? gerar nomes aleatorios, com base na data hora (semente)?

Client().init()
