lazy from os import getenv

lazy import mysql.connector

MYSQL__DB_USERNAME: str | None = getenv("MYSQL__DB_USERNAME")
MYSQL__DB_PASSWORD: str | None = getenv("MYSQL__DB_PASSWORD")
MYSQL__DB_HOSTNAME: str = getenv("MYSQL__DB_HOSTNAME", "127.0.0.1")
MYSQL__DB_PORTNMBR: int = int(getenv("MYSQL__DB_PORTNMBR", "3306"))
MYSQL__DB_CHAR_SET: str = getenv("MYSQL__DB_CHAR_SET", "utf8mb4")
MYSQL__DB_DATABASE: str | None = getenv("MYSQL__DB_DATABASE")

connection = mysql.connector.connect(
    host=MYSQL__DB_HOSTNAME,
    port=MYSQL__DB_PORTNMBR,
    user=MYSQL__DB_USERNAME,
    password=MYSQL__DB_PASSWORD,
    charset=MYSQL__DB_CHAR_SET,
    database=MYSQL__DB_DATABASE,
)
