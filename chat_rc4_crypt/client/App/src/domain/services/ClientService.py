import tkinter

from src.auxiliaries.constants.ClientConstants import *
from src.auxiliaries.helper.ClientHelper import *
from src.auxiliaries.utils.ClientUtil import *

class ClientService:
    def receive(socketClient, tkMsgList):
        """Handles receiving of messages."""

        while True:
            try:
                msgRecv = socketClient.recv(ClientConstants.BUFSIZE).decode(
                    ClientConstants.TEXT_ENCODE_SEND)

                msgRecv = ClientHelper.handlingIncomingMessages(msgRecv)

                tkMsgList.insert(tkinter.END, msgRecv)
                # Automatically scroll down Listbox in Tkinter
                tkMsgList.see(tkinter.END)
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
