import psycopg2
from flask import g


def init_app(app):
    app.teardown_appcontext(close_connection)


def get_connection():
    if 'connection' not in g:
        g.connection = psycopg2.connect(
            dbname='app', user='app', password='admin123', host='db'
        )
    return g.connection


def close_connection():
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()

