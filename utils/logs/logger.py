import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from utils.logs.logger_config import LoggerConfig


class Logger:

    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __handler_console = logging.StreamHandler()
    __formater_console = logging.Formatter(LoggerConfig.FORMAT)
    __handler_file = logging.FileHandler(LoggerConfig.LOGS_FILE_NAME)

    @staticmethod
    def info(message: str):
         Logger.__logger.info(msg=message)
    @staticmethod
    def debug(message: str):
        Logger.__logger.debug(msg=message)

    @staticmethod
    def warning(message: str):
        Logger.__logger.warning(msg=message)

    @staticmethod
    def error(message: str):
        Logger.__logger.error(msg=message)

    @staticmethod
    def critical(message: str):
        Logger.__logger.critical(msg=message)





