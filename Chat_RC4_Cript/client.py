"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter 
import RC4

nome = ''
flagNome = True
tipoCrip = 1

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            if(msg[0:3] == '$$$'):
                msg = msg.replace('$',"")
                msg_list.insert(tkinter.END, msg)
            else:
                msgDesencriptada = RC4.DesencriptarChat(msg)
                msg_list.insert(tkinter.END, msgDesencriptada)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()

    global flagNome
    if (flagNome):
        flagNome=False
        
        global nome
        nome = msg
    else:
        if(msg != '{quit}' and msg[0:7] != "{chave}"):
            msg = nome + ': ' + msg

    my_msg.set("")  # Clears input field.
    
    if(msg[0:7] == "{chave}"):
        if(msg[7]=='1'):
            chave = msg[8:]

            print('Tipo: RC4')
        
            arquivoChave= open('key.txt', 'w')
            arquivoChave.write(chave)
            arquivoChave.close()
            
            msg = 'Chave alterada por ' + nome
            
            msgEncriptada = RC4.EncriptarChat(msg) 
            client_socket.send(bytes(msgEncriptada, "utf8"))
        elif(msg[8]=='2'):
            print('Tipo 2')
        else:
            print('tipo invalido')
            
    elif(msg == "{quit}"):
        client_socket.send(bytes(msg, "utf8"))
        client_socket.close()
        top.quit()
    else:   
        msgEncriptada = RC4.EncriptarChat(msg) 
        client_socket.send(bytes(msgEncriptada, "utf8"))
            
def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
#my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
#HOST = input('Enter host: ')
#PORT = input('Enter port: ')

HOST = 'localhost'
PORT = '5354'
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop() # Starts GUI execution.