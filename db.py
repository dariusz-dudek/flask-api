import psycopg2
from flask import g


def get_connection():
    if 'connection' not in g:
        g.connection = psycopg2.connect(
            dbname='app', user='app', password='admin123', host='db'
        )
    return g.connection


def close_connection():
    connection = g.pop('')
