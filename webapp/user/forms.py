from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField("Запомнить меня",default=True,render_kw={"class":"form-check-input"})
    password = PasswordField('Пароль', validators=[DataRequired()],render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',render_kw={"class": "btn btn-primary"})