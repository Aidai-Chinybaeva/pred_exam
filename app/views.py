from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required

from app import db
from .models import Course, Student, User
from .forms import CourseForm, StudentForm, UserRegisterForm, UserLoginForm, StudentUpdateForm, CourseUpdateForm


def index():
    return 'Index'


def course_create():
    form = CourseForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_course = Course()
            form.populate_obj(new_course)
            db.session.add(new_course)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            print(form.errors)
    return render_template('form.html', form=form)


def course_list():
    course = Course.query.all()
    return render_template('course_list.html', course_list=course)


@login_required
def course_update(course_id):
    course = Course.query.get(course_id)
    form = CourseUpdateForm(obj=course)
    if request.method == 'POST':
        form.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('course_list'))
    else:
        print(form.errors)
    return render_template('/form.html', form=form)


@login_required
def course_delete(course_id):
    course = Course.query.get(course_id)
    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('course_list'))
    return render_template('/course_delete.html', course=course)


def student_list():
    st_list = Student.query.all()
    return render_template('student_list.html', st_list=st_list)


def student_create():
    form = StudentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_student = Student(
                name=form.name.data,
                course_id=form.course_id.data,
            )
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('student_list'))
        else:
            print(form.errors)
    return render_template('/form.html', form=form)


@login_required
def student_update(student_id):
    student = Student.query.get(student_id)
    form = StudentUpdateForm(meta={'csrf': False}, obj=student)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('student_list'))
        else:
            print(form.errors)
    return render_template('/form.html', form=form)


@login_required
def student_delete(student_id):
    student = Student.query.get(student_id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('student_list'))
    return render_template('/student_delete.html', student=student)


def user_register():
    form = UserRegisterForm()
    title = 'Регистрация'
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Пользователь {new_user.username} успешно зарегестрирован', 'Успех!')
            return redirect(url_for('user_login'))
        else:
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При регистрации пользователя произошла ошибка{". ".join(text_list)}', 'Ошибка!')

    return render_template('accounts/index.html', form=form, title=title)


def user_login():
    form = UserLoginForm()
    title = 'Авторизация'
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Вы успешно вошли в систему', 'Успех!')
                return redirect(url_for('transaction_list'))
            else:
                flash('Неверные логин и пароль', 'Ошибка!')

    return render_template('accounts/form.html', form=form, title=title)


def user_logout():
    logout_user()
    return redirect(url_for('user_login'))
