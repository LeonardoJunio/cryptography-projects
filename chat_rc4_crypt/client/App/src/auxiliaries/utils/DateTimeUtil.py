from datetime import datetime, timezone, timedelta

# 'object' would be the inheritance, don't need to make it explicit if it's this class
class DateTimeUtil(object):
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
