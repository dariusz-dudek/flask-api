from flask import Response, request
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
    status = repository.delete(author_id)

    if status == 'ok':
        return Response(dumps({
            'status': status
        }), mimetype='application/json', status=200)

    return status
