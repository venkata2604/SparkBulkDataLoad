class Log4J():
    def __init__(self, spark):
        log4J = spark.__javm.orh.apache.log4j
        self.logger = log4j.LogManager.getLogger("sdb1")

    def warn(self, message):
        self.logger.warn(message)

    def infor(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def debug (self, message):
        self.logger.debug(message)