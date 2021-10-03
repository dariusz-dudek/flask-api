from flask import Response, request, abort
from repositories.authors import AuthorsRepository
from json import dumps, loads


def authors_index():
    repository = AuthorsRepository()
    return Response(dumps(repository.get_all()), mimetype='application/json')


def authors_add():
    data = loads(request.data.decode('utf-8'))
    repository = AuthorsRepository()
    author_id = repository.add(data['first_name'], data['last_name'])

    return Response(dumps({
        'id': author_id
    }), mimetype='application/json', status=201)


def authors_delete(author_id):
    repository = AuthorsRepository()
    author = repository.get(author_id)

    if author is None:
        return abort(404)
    repository.delete(author_id)

    return Response(dumps({
        'status': 'ok'
    }), mimetype='application/json', status=200)
