from db import get_connection
from psycopg2 import extras
from flask import abort


class AuthorsRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def get_all(self):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors')
        return self.cursor.fetchall()

    def add(self, first_name, last_name):
        self.cursor.execute(
            'INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING id',
            (first_name, last_name)
        )
        author_id = self.cursor.fetchone()['id']
        self.connection.commit()
        return author_id

    def delete(self, author_id):
        self.cursor.execute('SELECT id, first_name, last_name FROM authors WHERE id=%s', (author_id,))
        author = self.cursor.fetchone()
        if author is None:
            return abort(404)

        self.cursor.execute('DELETE FROM authors WHERE id=%s', (author_id,))
        self.connection.commit()
        return 'ok'
