from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Course, User


def course_choices():
    choices = []
    with app.app_context():
        courses = Course.query.all()
        for course in courses:
            choices.append((course.id, course.language))
    return choices

class CourseForm(FlaskForm):
    language = wf.StringField(label='Язык программирования', validators=[
        wf.validators.DataRequired(),
    ])
    date_start = wf.DateField(label='Дата старта курса')
    date_end = wf.DateField(label='Дата окончания курса')


class StudentForm(FlaskForm):
    name = wf.StringField(label='ФиО', validators=[
        wf.validators.DataRequired(),
    ])
    course_id = wf.SelectField(label='Курсы', choices=course_choices)


class CourseUpdateForm(FlaskForm):
    language = wf.StringField(label='Язык программирования', validators=[
        wf.validators.DataRequired(),
    ])
    date_start = wf.DateField(label='Дата старта курса')
    date_end = wf.DateField(label='Дата окончания курса')


class StudentUpdateForm(FlaskForm):
    name = wf.StringField(label='ФиО', validators=[
        wf.validators.DataRequired(),
    ])
    course_id = wf.SelectField(label='Курсы', choices=course_choices)


class UserLoginForm(FlaskForm):
    username = wf.StringField(label='Логин', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=20)
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired(),
    ])

def validate_password(self, field):
    if len(field.data) < 8:
        raise wf.ValidationError('Длина пароля должна быть минимум 8 символов')


class UserRegisterForm(UserLoginForm):
    password2 = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired(),
    ])

def validate(self, *args, **kwargs):
    if not super().validate(*args, **kwargs):
        return False
    if self.password.data != self.password2.data:
        self.password2.errors.append('Пароли должны совпадать')
        return False
    return True

def validate_username(self, field):
    if User.query.filter_by(username=field.data).count() > 0:
        raise wf.ValidationError('Пользователь с таким username уже существует')

