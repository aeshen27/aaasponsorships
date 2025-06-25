import mysql.connector
import config

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
)
