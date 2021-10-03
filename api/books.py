from repositories.books import BooksRepository
from flask import Response, request, abort
from json import dumps, loads


def books_index():
    repository = BooksRepository()
    return Response(dumps(repository.get_all()), mimetype='application/json', status=200)


def books_add():
    data = loads(request.data.decode('utf-8'))
    repository = BooksRepository()
    book_id = repository.add(data['title'], data['author_id'])
    return Response(dumps({
        'id': book_id
    }), mimetype='application/json', status=201)


def books_delete(book_id):
    repository = BooksRepository()
    book = repository.get(book_id)
    if book is None:
        return abort(404)
    repository.delete(book_id)

    return Response(dumps({
        'status': 'ok'
    }), mimetype='application/json')
