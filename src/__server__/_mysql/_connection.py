from os import getenv
import mysql.connector

MYSQL__DB_USERNAME: str | None = getenv("MYSQL__DB_USERNAME")
MYSQL__DB_PASSWORD: str | None = getenv("MYSQL__DB_PASSWORD")
MYSQL__DB_HOSTNAME: str | None = getenv("MYSQL__DB_HOSTNAME")
MYSQL__DB_PORTNMBR: int | None = int(getenv("MYSQL__DB_PORTNMBR", "3306"))
MYSQL__DB_CHAR_SET: str | None = getenv("MYSQL__DB_CHAR_SET")
MYSQL__DB_DATABASE: str | None = getenv("MYSQL__DB_DATABASE")


connection = mysql.connector.connect(
    host=MYSQL__DB_HOSTNAME,
    port=MYSQL__DB_PORTNMBR,
    user=MYSQL__DB_USERNAME,
    charset=MYSQL__DB_CHAR_SET,
    password=MYSQL__DB_PASSWORD,
    database=MYSQL__DB_DATABASE,
)
