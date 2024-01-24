import mysql.connector as mysql
from config_server import DATABASE_CONFIG

def connect_to_db():
    config = DATABASE_CONFIG
    return mysql.connect(**config)

def close_db_connection(db):
    db.close()