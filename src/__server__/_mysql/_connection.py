from os import getenv
import mysql.connector

MYSQL__DB_USERNAME: str | None = getenv("MYSQL__DB_USERNAME")
MYSQL__DB_PASSWORD: str | None = getenv("MYSQL__DB_PASSWORD")
MYSQL__DB_HOSTNAME: str | None = getenv("MYSQL__DB_HOSTNAME")
MYSQL__DB_PORTNMBR: str | None = getenv("MYSQL__DB_PORTNMBR")
MYSQL__DB_CHAR_SET: str | None = getenv("MYSQL__DB_CHAR_SET")
MYSQL__DB_DATABASE: str | None = getenv("MYSQL__DB_DATABASE")
