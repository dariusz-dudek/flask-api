from repositories.users import UsersRepository
from flask import render_template, request
from hashlib import pbkdf2_hmac
from forms import RegisterForm, LoginForm


def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        crypted_password = crypt_password(form.password.data)

        repository = UsersRepository()
        user = repository.get_by_username(username)
        print(user['password'])
        print(crypted_password)
        quit()

    return render_template('login.html', form=form)


def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = crypt_password(form.password.data)

        repository = UsersRepository()
        repository.add(username, password)
    return render_template('register.html', form=form)


def crypt_password(password):
    salt = 'abcdef1234!@#$%'
    password = pbkdf2_hmac(
        'sha256',
        password.encode('utf8'),
        salt.encode('utf8'),
        999
    )
    return password.hex()
