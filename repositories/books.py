from db import get_connection
from psycopg2 import extras
from flask import abort


class BooksRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def get_all(self):
        self.cursor.execute('SELECT id, title, author_id FROM app.public.books')
        return self.cursor.fetchall()

    def add(self, title, author_id):
        self.cursor.execute(
            'INSERT INTO app.public.books (title, author_id) VALUES (%s, %s) returning id',
            (title, author_id))
        book_id = self.cursor.fetchone()['id']
        self.connection.commit()
        return book_id

    def delete(self, book_id):
        self.cursor.execute(
            'SELECT id, title, author_id FROM app.public.books WHERE id=%s',
            (book_id,)
        )
        book = self.cursor.fetchone()
        if book is None:
            return abort(404)
        self.cursor.execute('DELETE FROM app.public.books WHERE id=%s', (book_id,))
        self.connection.commit()
        return 'ok'

