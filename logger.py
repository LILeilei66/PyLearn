import os
import inspect
import logging


innerLogFormat = "%(asctime)s - %(levelname)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=innerLogFormat, filename='./log/log.txt',
                    filemode='a')
#logging.basicConfig(level=logging.DEBUG, format=innerLogFormat, filename="./log/log.txt", filemode="w")

class Logger():
    @staticmethod
    def InnerBuildLogPrefix():
        stack = inspect.stack()
        filePath = stack[2][1]
        fileName = os.path.basename(filePath).split(".")[0]
        funcName = stack[2][3]
        prefix = fileName + ": " + funcName + "() "
        print(stack)
        print(filePath)
        print(funcName)
        return prefix

    @classmethod
    def SetLogLevel(cls, logLevel):
        logging.basicConfig(logLevel, format=innerLogFormat)

    @classmethod
    def LogCritical(cls, log_content):
        logging.critical(cls.InnerBuildLogPrefix() + log_content)

    @classmethod
    def LogError(cls, log_content):
        logging.error(cls.InnerBuildLogPrefix() + log_content)

    @classmethod
    def LogWarning(cls, log_content):
        logging.warning(cls.InnerBuildLogPrefix() + log_content)

    @classmethod
    def LogInfo(cls, log_content):
        logging.info(cls.InnerBuildLogPrefix() + log_content)

    @classmethod
    def LogDebug(cls, log_content):
        logging.debug(cls.InnerBuildLogPrefix() + log_content )

class LogTest():
    def __init__(self):
        pass

    def test_log_critical(self, log_content):
        Logger.LogCritical(log_content)

if __name__ == '__main__':
    log_test = LogTest()
    log_test.test_log_critical('test log_critical')
