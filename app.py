from flask import Flask
from api.authors import authors_add, authors_delete, authors_index
from api.books import books_index, books_add, books_delete
from controlers import login, register

app = Flask(__name__)


app.add_url_rule('/authors', view_func=authors_index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors_add, methods=['POST'])
app.add_url_rule('/authors/<author_id>', view_func=authors_delete, methods=['DELETE'])

app.add_url_rule('/books', view_func=books_index, methods=['GET'])
app.add_url_rule('/books', view_func=books_add, methods=['POST'])
app.add_url_rule('/books/<book_id>', view_func=books_delete, methods=['DELETE'])

app.add_url_rule('/login', view_func=login, methods=['POST', 'GET'])
app.add_url_rule('/register', view_func=register, methods=['POST', 'GET'])
