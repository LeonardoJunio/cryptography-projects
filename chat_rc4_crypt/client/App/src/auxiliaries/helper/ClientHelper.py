from src.auxiliaries.constants.ClientConstants import *
from src.auxiliaries.utils.DateTimeUtil import *
from src.auxiliaries.utils.ClientUtil import *
from src.domain.services.Rc4CryptService import *

class ClientHelper:
    def handlingIncomingMessages(msg):
        if (msg[0:3] == ClientConstants.TEXT_PREFIX):
            return msg.replace('$', "-")

        return Rc4CryptService.decrypt(msg)

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

                msgEncrypted = Rc4CryptService.encrypt(msgInput)
                socketClient.send(ClientUtil.convertStrBytes(msgEncrypted))
            else:
                print("Crypt not defined", flush=True)

            return

        msgEncrypted = Rc4CryptService.encrypt(timeNow + msgInput)
        socketClient.send(ClientUtil.convertStrBytes(msgEncrypted))
