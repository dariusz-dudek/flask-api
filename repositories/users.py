from db import get_connection
from psycopg2 import extras
from auth import User


class UsersRepository:
    def __init__(self):
        self.connection = get_connection()
        self.cursor = self.connection.cursor(cursor_factory=extras.RealDictCursor)

    def map_row_to_user(self, row):
        user = User()
        user.id = row['id']
        user.username = row['username']
        user.password = row['password']

        return user

    def get_by_username(self, username):
        self.cursor.execute('SELECT id, username, password FROM app.public.users WHERE username=%s', (username,))
        return self.map_row_to_user(
            self.cursor.fetchone()
        )

    def get_by_id(self, user_id):
        self.cursor.execute('SELECT id, username, password FROM app.public.users where id=%s', (user_id,))
        return self.map_row_to_user(
            self.cursor.fetchone()
        )

    def add(self, username, password):
        self.cursor.execute(
            'INSERT INTO app.public.users (username, password) VALUES (%s, %s) RETURNING id',
            (username, password)
        )
        user_id = self.cursor.fetchone()
        self.connection.commit()
        return user_id['id']
