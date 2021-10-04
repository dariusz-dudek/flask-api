from dotenv import load_dotenv
from os import getenv
from flask import g
import psycopg2


load_dotenv()


def init_app(app):
    app.teardown_appcontext(close_connection)


def get_connection():
    if 'connection' not in g:
        g.connection = psycopg2.connect(
            dbname=getenv('DB_NAME', 'app'),
            user=getenv('DB_USER', 'app'),
            password=getenv('DB_PASSWORD', 'admin123'),
            host=getenv('DB_HOST', 'db')
        )
    return g.connection


def close_connection():
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()
