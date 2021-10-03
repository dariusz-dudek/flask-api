from db import get_connection
from psycopg2 import extras


class UsersRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def get_by_username(self, username):
        self.cursor.execute('SELECT id, username, password FROM app.public.users WHERE username=%s', (username,))
        return self.cursor.fetchone()

    def add(self, username, password):
        self.cursor.execute(
            'INSERT INTO app.public.users (username, password) VALUES (%s, %s) RETURNING id',
            (username, password)
        )
        user_id = self.cursor.fetchone()
        self.connection.commit()
        return user_id['id']
