from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.home.forms import LoginFrom, ChangePasswordForm
from app.models import User, LoginLog
from app import db
from functools import wraps
from datetime import datetime


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def login_log_add(user_id, operation_type, ip_address):
    try:
        login_log = LoginLog(
            user_id=user_id,
            operation_type=operation_type,
            ip=ip_address,
            create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(login_log)
        db.session.commit()
    except Exception as e:
        print(e)


@home.route('/', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(username=data['username']).first()
        if not user.check_password(data['password']):
            flash(message='密码输入有误,请重新输入')
            return redirect(url_for('home.login'))
        session['user'] = data['username']
        login_log_add(user_id=user.id, operation_type='登录', ip_address=request.remote_addr)
        return redirect(request.args.get('next') or url_for('home.index'))
    return render_template('home/login.html', form=form)


@home.route('/index/')
@login_required
def index():
    return render_template('home/index.html')


@home.route('/logout/', methods=['GET'])
@login_required
def logout():
    user = User.query.filter_by(username=session['user']).first()
    session.pop('user', None)
    login_log_add(user_id=user.id,operation_type='登出',ip_address=request.remote_addr)
    return redirect(url_for('home.login'))


@home.route('/change_password/', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        data = form.data
        try:
            user = User.query.filter_by(username=session['user']).first()
            from werkzeug.security import generate_password_hash
            user.password = generate_password_hash(data['new_password'])
            db.session.add(user)
            db.session.commit()
            login_log_add(user_id=user.id,operation_type='修改密码',ip_address=request.remote_addr)
            flash(message='修改密码成功，请重新登录', category='ok')
            return redirect(url_for('home.logout'))
        except Exception as e:
            print(e)
    return render_template('home/change_password.html', form=form)
