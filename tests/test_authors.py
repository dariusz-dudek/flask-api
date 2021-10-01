import requests


def test_get_authors():
    response = requests.get('http://localhost:5000/authors')
    assert response.status_code == 200

    # Czy po dodaniu autora mam o jednego autora więcej


def test_add_author():
    payload = {
        'first_name': 'Grzegorz',
        'last_name': 'Brzęczyszczykiewicz'
    }
    response = requests.post('http://localhost:5000/authors', payload)
    assert response.status_code == 201

    response = requests.post('http://localhost:5000/authors', payload)
    data = response.json()
    assert data[-1]['first_name'] == 'Grzegorz'
    assert data[-1]['last_name'] == 'Brzęczyszczykiewicz'


# Czy po usunięciu autora mam o jednego autora mniej

def test_delete_author():
    response = requests.get('http://localhost:5000/authors')
    data = response.json()
    quantity = len(data)
    last_id = data[-1]['id']

    requests.delete(f'http://localhost:5000/authors/<{last_id}>')
    response = requests.get('http://localhost:5000/authors')
    data = response.json()
    new_quantity = len(data)
    assert new_quantity + 1 == quantity

