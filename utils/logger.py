import logging
from logging.handlers import TimedRotatingFileHandler


class logger():
    def __init__(self, logger_name):
        logging.getLogger(logger_name)
        log_fmt = '%(asctime)s:%(levelname)s:%(message)s [%(pathname)s][Line:%(lineno)d][PID:%(process)d]'
        formatter = logging.Formatter(log_fmt)
        log_file_handler = TimedRotatingFileHandler(filename='peppa_gitscan.log', when="D", interval=1, backupCount=30)
        log_file_handler.setFormatter(formatter)
        self.log = logging.getLogger()
        logging.basicConfig(level=logging.INFO)
        self.log.addHandler(log_file_handler)

    def critical(self, msg):
        self.log.critical(msg)

    def error(self, msg):
        self.log.error(msg)

    def warn(self, msg):
        self.log.warning(msg)

    def info(self, msg):
        self.log.info(msg)


if __name__ == '__main__':
    test = logger(__name__)
    test.error('error_test')