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
tipoCrip = 1

TEXT_PREFIX = "$$$"


def clearInputField():
    tkMsgStrVar.set("")


def receive():
    """Handles receiving of messages."""

    while True:
        try:
            msg = socketClient.recv(BUFSIZE).decode("utf8")

            if (msg[0:3] == TEXT_PREFIX):
                msg = msg.replace('$', "-")
                tkMsgList.insert(tkinter.END, msg)
            else:
                msgDecrypted = RC4.DesencriptarChat(msg)
                tkMsgList.insert(tkinter.END, msgDecrypted)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = tkMsgStrVar.get().strip()

    if not msg:
        clearInputField()
        return

    global flagNome
    if (flagNome):
        flagNome = False

        global nome
        nome = msg
    else:
        if (msg != '{quit}' and msg[0:7] != "{chave}"):
            msg = nome + ': ' + msg

    clearInputField()

    if (msg[0:7] == "{chave}"):
        if (msg[7] == '1'):
            chave = msg[8:]

            print('Tipo: RC4')

            arquivoChave = open('key.txt', 'w')
            arquivoChave.write(chave)
            arquivoChave.close()

            msg = 'Chave alterada por ' + nome

            msgEncriptada = RC4.EncriptarChat(msg)
            socketClient.send(bytes(msgEncriptada, "utf8"))
        elif (msg[8] == '2'):  # 7 ou 8?
            print('Tipo 2')
        else:
            print('tipo invalido')

    elif (msg == "{quit}"):
        socketClient.send(bytes(msg, "utf8"))
        socketClient.close()
        tkTop.quit()
    else:
        msgEncriptada = RC4.EncriptarChat(msg)
        socketClient.send(bytes(msgEncriptada, "utf8"))


def onClosing(event=None):
    """This function is to be called when the window is closed."""

    tkMsgStrVar.set("{quit}")
    send()


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
tkMsgList.pack()
tkMsgFrame.pack()

tkMsgEntryField = tkinter.Entry(tkTop, textvariable=tkMsgStrVar)
tkMsgEntryField.bind("<Return>", send)
tkMsgEntryField.pack()
tkSendButton = tkinter.Button(tkTop, text="Send", command=send)
tkSendButton.pack()

tkTop.protocol("WM_DELETE_WINDOW", onClosing)

HOST = '0.0.0.0'
PORT = 5354
BUFSIZE = 1024

socketClient = socket(AF_INET, SOCK_STREAM)
socketClient.connect((HOST, PORT))

threadReceive = Thread(target=receive)
# A thread that runs in the background, and is not expected to complete its execution before the program exits.
# On the other hand, non-daemon threads are critical to the functioning of the program,
# and they prevent the main program from exiting until they have completed their execution
# The Daemon Thread does not block the main thread from exiting and continues to run in the background.
threadReceive.daemon = True
threadReceive.start()
# Starts GUI execution
tkinter.mainloop()
