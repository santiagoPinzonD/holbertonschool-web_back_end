#!/usr/bin/env python3
""" module for filter_datum function """

import re
import logging
import mysql.connector
import os

from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ function that format the record """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function that return a message obfuscated """
    for msj in fields:
        message = re.sub(
            f"(?<={msj}=).*?(?={separator})", redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ function that return a logger object """
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False

    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    log.addHandler(stream)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    connect to the MySQL database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    conect = mysql.connector.connection.MySQLConnection(
        host=host,
        user=username,
        password=password,
        database=db
    )
    return conect


def main():
    """ get data from database """
    data = get_db()
    myCursor = data.cursor()
    myCursor.execute("SELECT * FROM users")
    description = [desc[0] for desc in myCursor.description]

    logger = get_logger()

    for user in myCursor:
        userInfo = "".join(
            f'{des}={str(usr)}; ' for usr, des in zip(user, description)
        )
        logger.info(userInfo)

    myCursor.close()
    data.close()


if __name__ == '__main__':
    main()
