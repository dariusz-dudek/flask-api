from api.authors import authors_add, authors_delete, authors_index
from api.books import books_index, books_add, books_delete
from repositories.users import UsersRepository
from controlers import login, register, logout, home
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '@@wwaasWQ((&#&#JKNQJQNWEIO)@*#!'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    repo = UsersRepository()
    return repo.get_by_id(user_id)


app.add_url_rule('/authors', view_func=authors_index, methods=['GET'])
app.add_url_rule('/authors', view_func=authors_add, methods=['POST'])
app.add_url_rule('/authors/<author_id>', view_func=authors_delete, methods=['DELETE'])

app.add_url_rule('/books', view_func=books_index, methods=['GET'])
app.add_url_rule('/books', view_func=books_add, methods=['POST'])
app.add_url_rule('/books/<book_id>', view_func=books_delete, methods=['DELETE'])

app.add_url_rule('/home', view_func=home, methods=['GET'])
app.add_url_rule('/login', view_func=login, methods=['POST', 'GET'])
app.add_url_rule('/logout', view_func=logout, methods=['GET'])
app.add_url_rule('/register', view_func=register, methods=['POST', 'GET'])
