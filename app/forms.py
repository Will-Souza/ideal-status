from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[
        InputRequired('Digite um nome de usuário')
    ])
    password = PasswordField('Senha', validators=[
        InputRequired('Digite uma senha')
    ])
    remember = BooleanField()
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    name = StringField('Nome', validators=[
        InputRequired('Digite um nome')
    ])
    username = StringField('Nome de usuário', validators=[
        Length(min=4, max=25, message='O nome de usuário deve conter entre 3 e 32 caracteres'),
        InputRequired('Digite um nome de usuário')
    ])
    email = StringField('E-mail', validators=[
        Length(min=6, max=32, message='O e-mail deve conter entre 6 e 32 caracteres'),
        InputRequired('Digite seu e-mail')
    ])
    password = PasswordField('Senha', validators=[
        InputRequired('Digite uma senha'),
        EqualTo('confirm', message='As senhas estão diferentes')
    ])
    confirm = PasswordField('Confirme a senha', validators=[
        InputRequired('Digite a senha novamente')
    ])
    submit = SubmitField('Cadastrar')
    cancel = SubmitField('Cancelar')
