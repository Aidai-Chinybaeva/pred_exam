from app import app

from . import views

app.add_url_rule('/', view_func=views.index)

app.add_url_rule('/course/create', view_func=views.course_create, methods=['POST', 'GET'])
app.add_url_rule('/student/create', view_func=views.student_create, methods=['POST', 'GET'])
app.add_url_rule('/course/list', view_func=views.course_list)
app.add_url_rule('/student/list', view_func=views.student_list)

app.add_url_rule('/course/<int:course_id>/update', view_func=views.course_update, methods=['POST', 'GET']),
app.add_url_rule('/course/<int:course_id>/delete', view_func=views.course_delete, methods=['POST', 'GET']),

app.add_url_rule('/student/list', view_func=views.course_list)
app.add_url_rule('/student/<int:student_id>/update', view_func=views.student_update, methods=['POST', 'GET']),
app.add_url_rule('/student/<int:student_id>/delete', view_func=views.student_delete, methods=['POST', 'GET']),

app.add_url_rule('/account/register', view_func=views.user_register, methods=['POST', 'GET'])
app.add_url_rule('/account/login', view_func=views.user_login, methods=['POST', 'GET'])
app.add_url_rule('/account/logout', view_func=views.user_logout)
