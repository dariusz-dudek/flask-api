from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('Nazwa użytkownika: ', [validators.Length(min=5)])
    password = PasswordField('Hasło: ', [
        validators.Length(min=8),
        validators.EqualTo('password_repeat')
    ])
    password_repeat = PasswordField('Powtórz hasło: ')


class LoginForm(Form):
    username = StringField('Nazwa użytkownika: ', [validators.Length(min=5)])
    password = PasswordField('Hasło: ', [validators.Length(min=8)])


