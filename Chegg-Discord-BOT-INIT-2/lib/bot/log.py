from datetime import datetime as dt

class Log:
    def __init__(self, path, logName):
        self.log = f"{dt.now()}::"
        self.path = path
        self.logName = logName

    def loging(self, fullLog):
        fileName = r"{0}\{1}".format(self.path,self.logName)
        logFile = open(fileName,"a+",encoding="utf-8")
        logFile.write(fullLog+"\n")
        logFile.close()

    def alert(self, log):
        alertLog = "ALERT::"
        alertLog += self.log + str(log)
        self.loging(alertLog)

    def info(self, log):
        infoLog = "INFO::"
        infoLog += self.log + str(log)
        self.loging(infoLog)

    def command(self,log):
        commandLog = "COMMAND::"
        commandLog += self.log + str(log)
        self.loging(commandLog)
