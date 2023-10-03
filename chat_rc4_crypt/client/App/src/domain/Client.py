"""Script for Tkinter GUI chat client."""

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

from src.auxiliaries.constants.ClientConstants import *
from src.domain.services.ClientService import *
from src.domain.ClientUser import *

class Client:
    def init(self):
        user = ClientUser()

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
