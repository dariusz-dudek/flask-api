import requests


def test_get_books():
    response = requests.get('http://localhost:5000/books')
    assert response.status_code == 200

    # Czy po dodaniu autora mam o jednego autora więcej


def test_add_book():
    payload = {
        'title': 'Ogniem i mieczem',
        'author_id': 1
    }
    response = requests.post('http://localhost:5000/books', json=payload)
    assert response.status_code == 201

    response = requests.get('http://localhost:5000/books')
    data = response.json()
    assert data[-1]['title'] == 'Ogniem i mieczem'
    assert data[-1]['author_id'] == 1


def test_add_wrong_book():
    payload = {
        'title': 'Ogniem i mieczem',
    }
    response = requests.post('http://localhost:5000/books', json=payload)
    assert response.status_code == 400


# Czy po usunięciu autora mam o jednego autora mniej

def test_delete_book():
    response = requests.get('http://localhost:5000/books')
    data = response.json()
    quantity = len(data)
    last_id = data[-1]['id']

    requests.delete(f'http://localhost:5000/books/{last_id}')

    response = requests.get('http://localhost:5000/books')
    data = response.json()
    new_quantity = len(data)
    assert new_quantity + 1 == quantity

