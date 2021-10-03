from repositories.books import BooksRepository
from flask import Response, request, abort
from pydantic import ValidationError
from json import dumps, loads
from models import Book


def books_index():
    repository = BooksRepository()
    return Response(dumps(repository.get_all()), mimetype='application/json', status=200)


def books_add():
    repository = BooksRepository()
    data = loads(request.data.decode('utf-8'))
    try:
        book = Book(**data)
        book_id = repository.add(book.title, book.author_id)
        return Response(dumps({
            'id': book_id
        }), mimetype='application/json', status=201)
    except ValidationError as error:
        return Response(
            error.json(),
            mimetype='application/json',
            status=400
        )


def books_delete(book_id):
    repository = BooksRepository()
    book = repository.get(book_id)
    if book is None:
        return abort(404)
    repository.delete(book_id)

    return Response(dumps({
        'status': 'ok'
    }), mimetype='application/json')
