import os
import mysql.connector
from . import CONFIGURATION_JSON, MYSQL__DB_PASSWORD

# Database Connection
connection = mysql.connector.connect(
    host="localhost",
    password=MYSQL__DB_PASSWORD,
    user=CONFIGURATION_JSON["MySQL Credentials"]["USERNAME"],
    database=CONFIGURATION_JSON["MySQL Credentials"]["DATABASE"],
)


class SERVER:

    cursor = connection.cursor()

    class table_definition:

        def __init__(self):

            self.cursor = SERVER.cursor
