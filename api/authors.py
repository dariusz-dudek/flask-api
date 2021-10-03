from repositories.authors import AuthorsRepository
from flask import Response, request, abort
from pydantic import ValidationError
from json import dumps, loads
from models import Author


def authors_index():
    repository = AuthorsRepository()
    return Response(dumps(repository.get_all()), mimetype='application/json')


def authors_add():
    repository = AuthorsRepository()
    data = loads(request.data.decode('utf-8'))
    try:
        author = Author(**data)

        author_id = repository.add(author.first_name, author.last_name)

        return Response(dumps({
            'id': author_id
        }), mimetype='application/json', status=201)

    except ValidationError as error:
        return Response(
            error.json(),
            mimetype='application/json',
            status=400
        )


def authors_delete(author_id):
    repository = AuthorsRepository()
    author = repository.get(author_id)

    if author is None:
        return abort(404)
    repository.delete(author_id)

    return Response(dumps({
        'status': 'ok'
    }), mimetype='application/json', status=200)
