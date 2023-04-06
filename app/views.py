from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required


def index():
    return 'Index'