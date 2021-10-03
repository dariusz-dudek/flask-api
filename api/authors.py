from psycopg2 import extras
from flask import Response, request, abort
from db import get_connection
from json import dumps, loads


def index():
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('SELECT id, first_name, last_name FROM authors')

    return Response(dumps(cursor.fetchall()), mimetype='application/json')


def add():
    data = loads(request.data.decode('utf-8'))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING id',
        (data['first_name'], data['last_name'])
    )
    author_id = cursor.fetchone()[0]
    connection.commit()

    return Response(dumps({
        'id': author_id
    }), mimetype='application/json', status=201)


def delete(author_id):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('SELECT id, first_name, last_name FROM authors WHERE id=%s', (author_id,))

    author = cursor.fetchone()
    if author is None:
        return abort(404)

    cursor.execute('DELETE FROM authors WHERE id=%s', (author_id,))
    connection.commit()

    return Response(dumps({
        'status': 'ok'
    }), mimetype='application/json', status=200)
