from . import users
from flask import render_template, flash, redirect, url_for, request, session
from app.users.forms import UserForm, GroupForm, RoleForm, AuthForm
from app.models import User, Group, Role, Auth, LoginLog
from app import db
from werkzeug.security import generate_password_hash
from app.home.views import login_required, login_log_add

# 用户列表
@users.route('/user_list/<int:page>/', methods=['GET'])
@login_required
def user_list(page=None):
    if page is None:
        page = 1
    page_data = User.query.order_by(User.id.desc()).paginate(page=page, per_page=10)
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='查询用户', ip_address=request.remote_addr)
    return render_template('users/user_list.html', page_data=page_data)


# 添加用户
@users.route('/user_add/', methods=['GET', 'POST'])
@login_required
def user_add():
    form = UserForm()
    form.group.choices = [(v.id, v.name) for v in Group.query.all()]
    form.role.choices = [(v.id, v.name) for v in Role.query.all()]
    if form.validate_on_submit():
        data = form.data
        if User.query.filter_by(username=data['username']).count() == 1:
            flash(message='该用户已存在，请添加其他用户', category='error')
            return redirect(url_for('users.user_add'))
        else:
            try:
                user = User(
                    username=data['username'],
                    password=generate_password_hash(data['password']),
                    name=data['name'],
                    email=data['email'],
                    phone=data['phone'],
                    company_name=data['company_name'],
                    is_active=data['is_active'],
                    is_admin=data['is_admin'],
                    remark=data['remark'],
                )
                db.session.add(user)
                db.session.commit()
                user_name = User.query.filter_by(username=data['username']).first_or_404()
                for group_id in data['group']:
                    choise_group = Group.query.filter_by(id=group_id).first_or_404()
                    user_name.groups.append(choise_group)
                for role_id in data['role']:
                    choise_role = Role.query.filter_by(id=role_id).first_or_404()
                    user_name.roles.append(choise_role)
                db.session.add(user_name)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='添加用户', ip_address=request.remote_addr)
                flash(message='添加用户成功！', category='ok')
                return redirect(url_for('users.user_add'))
            except Exception as e:
                print(e)
                flash(message='添加用户失败', category='error')
                return redirect(url_for('users.user_add'))
    else:
        pass
    return render_template('users/user_add.html', form=form)


# 编辑用户
@users.route('/user_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def user_edit(id=None):
    form = UserForm()
    form.group.choices = [(v.id, v.name) for v in Group.query.all()]
    form.role.choices = [(v.id, v.name) for v in Role.query.all()]
    user = User.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        user_count = User.query.filter_by(name=data['name']).count()
        if user.name != data['name'] and user_count == 1:
            flash(message='该用户组已存在，请重新输入', category='error')
            return redirect(url_for('users.user_edit', id=id))
        else:
            try:
                user.username = data['username']
                user.password = generate_password_hash(data['password'])
                user.name = data['name']
                user.email = data['email']
                user.phone = data['phone']
                user.company_name = data['company_name']
                user.is_active = data['is_active']
                user.is_admin = data['is_admin']
                user.remark = data['remark']
                db.session.add(user)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='编辑用户', ip_address=request.remote_addr)
                flash(message='修改用户信息成功', category='ok')
                return redirect(url_for('users.user_edit', id=id))
            except Exception as e:
                print(e)
                flash(message='修改用户信息失败', category='error')
                return redirect(url_for('users.user_edit', id=id))
    else:
        pass
    return render_template('users/user_edit.html', form=form, user=user)


# 删除用户
@users.route('/user_delete/<int:id>/', methods=['GET'])
@login_required
def user_delete(id=None):
    user = User.query.filter_by(id=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='删除用户', ip_address=request.remote_addr)
    flash(message='删除用户成功', category='ok')
    return render_template('users/user_list.html', page=1)


# 用户组列表
@users.route('/group_list/<int:page>/', methods=['GET'])
@login_required
def group_list(page=None):
    if page is None:
        page = 1
    page_data = Group.query.order_by(Group.id.desc()).paginate(page=page, per_page=10)
    user = User.query.filter_by(username=session['user']).first()
    login_log_add(user_id=user.id, operation_type='查询用户组', ip_address=request.remote_addr)
    return render_template('users/group_list.html', page_data=page_data)


# 添加用户组
@users.route('/group_add/', methods=['GET', 'POST'])
@login_required
def group_add():
    form = GroupForm()
    form.roles.choices = [(v.id, v.name) for v in Role.query.all()]
    if form.validate_on_submit():
        data = form.data
        group_count = Group.query.filter_by(name=data['name']).count()
        if group_count == 1:
            flash(message='该用户组已存在，请重新输入', category='error')
            return redirect(url_for('users.group_add'))
        else:
            try:
                group = Group(
                    name=data['name'],
                    is_admin=data['is_admin'],
                )
                db.session.add(group)
                db.session.commit()
                group_name = Group.query.filter_by(name=data['name']).first_or_404()
                for role_id in data['roles']:
                    choise_role = Role.query.filter_by(id=role_id).first_or_404()
                    group_name.roles.append(choise_role)
                db.session.add(group_name)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='添加用户组', ip_address=request.remote_addr)
                flash(message='添加用户组成功', category='ok')
                return redirect(url_for('users.group_add'))
            except Exception as e:
                print(e)
                flash(message='添加用户组失败', category='error')
                return redirect(url_for('users.group_add'))
    else:
        pass
    return render_template('users/group_add.html', form=form)


# 编辑用户组
@users.route('/group_edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def group_edit(id=None):
    form = GroupForm()
    form.roles.choices = [(v.id, v.name) for v in Group.query.all()]
    group = Group.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        group_count = Group.query.filter_by(name=data['name']).count()
        if group.name != data['name'] and group_count == 1:
            flash(message='该用户组已存在，请重新输入', category='error')
            return redirect(url_for('users.group_edit', id=id))
        else:
            try:
                group.name = data['name']
                group.is_admin = data['is_admin']
                group.auths = data['auths']
                db.session.add(group)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='编辑用户组', ip_address=request.remote_addr)
                flash(message='添加权限成功', category='ok')
                return redirect(url_for('users.group_edit', id=id))
            except Exception as e:
                print(e)
                flash(message='添加权限失败', category='error')
                return redirect(url_for('users.group_edit', id=id))
    else:
        pass
    return render_template('users/group_edit.html', form=form, group=group)


# 删除用户组
@users.route('/group_delete/<int:id>/', methods=['GET'])
@login_required
def group_delete(id=None):
    group = Group.query.filter_by(id=id).first_or_404()
    db.session.delete(group)
    db.session.commit()
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='删除用户组', ip_address=request.remote_addr)
    flash(message='删除用户组成功', category='ok')
    return render_template('users/group_list.html', page=1)


# 角色列表
@users.route('/role_list/<int:page>/', methods=['GET'])
@login_required
def role_list(page=None):
    if page is None:
        page = 1
    page_data = Role.query.order_by(Role.id.desc()).paginate(page=page, per_page=10)
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='查询角色', ip_address=request.remote_addr)
    return render_template('users/role_list.html', page_data=page_data)


# 添加角色
@users.route('/role_add/', methods=['GET', 'POST'])
@login_required
def role_add():
    form = RoleForm()
    form.auths.choices = [(v.id, v.name) for v in Auth.query.all()]
    if form.validate_on_submit():
        data = form.data
        role_count = Role.query.filter_by(name=data['name']).count()
        if role_count == 1:
            flash(message='该角色已存在，请重新输入', category='error')
            return redirect(url_for('users.role_add'))
        else:
            try:
                role = Role(
                    name=data['name'],
                    is_admin=data['is_admin'],
                )
                db.session.add(role)
                db.session.commit()
                role_name = Role.query.filter_by(name=data['name']).first_or_404()
                for auth_id in data['auths']:
                    choise_auth = Auth.query.filter_by(id=auth_id).first_or_404()
                    role_name.auths.append(choise_auth)
                db.session.add(role_name)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='添加角色', ip_address=request.remote_addr)
                flash(message='添加角色成功', category='ok')
                return redirect(url_for('users.role_add'))
            except Exception as e:
                print(e)
                flash(message='添加角色失败', category='error')
                return redirect(url_for('users.role_add'))
    else:
        pass
    return render_template('users/role_add.html', form=form)


# 编辑角色
@users.route('/role_edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def role_edit(id=None):
    form = RoleForm()
    form.auths.choices = [(v.id, v.name) for v in Auth.query.all()]
    role = Role.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        role_count = Auth.query.filter_by(name=data['name']).count()
        if role.name != data['name'] and role_count == 1:
            flash(message='该角色已存在，请重新输入', category='error')
            return redirect(url_for('users.role_edit', id=id))
        else:
            try:
                role.name = data['name']
                role.is_admin = data['is_admin']
                role.auths = data['auths']
                db.session.add(role)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='编辑角色', ip_address=request.remote_addr)
                flash(message='添加权限成功', category='ok')
                return redirect(url_for('users.role_edit', id=id))
            except Exception as e:
                print(e)
                flash(message='添加权限失败', category='error')
                return redirect(url_for('users.role_edit', id=id))
    else:
        pass
    return render_template('users/role_edit.html', form=form, role=role)


# 删除角色
@users.route('/role_delete/<int:id>', methods=['GET'])
@login_required
def role_delete(id=None):
    role = Role.query.filter_by(id=id).first_or_404()
    db.session.delete(role)
    db.session.commit()
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='删除角色', ip_address=request.remote_addr)
    flash(message='删除角色成功', category='ok')
    return render_template('users/role_list.html', page=1)


# 权限列表
@users.route('/auth_list/<int:page>/', methods=['GET'])
@login_required
def auth_list(page=None):
    if page is None:
        page = 1
    page_data = Auth.query.order_by(Auth.id.desc()).paginate(page=page, per_page=10)
    user = User.query.filter_by(username=session['user']).first_or_404()
    login_log_add(user_id=user.id, operation_type='查询权限', ip_address=request.remote_addr)
    return render_template('users/auth_list.html', page_data=page_data)


# 添加权限
@users.route('/auth_add/', methods=['GET', 'POST'])
@login_required
def auth_add():
    form = AuthForm()
    if form.validate_on_submit():
        data = form.data
        auth_count = Auth.query.filter_by(name=data['name']).count()
        if auth_count == 1:
            flash(message='该权限已存在，请重新输入', category='error')
            return redirect(url_for('users.auth_add'))
        else:
            try:
                auth = Auth(
                    name=data['name'],
                    url=data['url'],
                )
                db.session.add(auth)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='添加权限', ip_address=request.remote_addr)
                flash(message='添加权限成功', category='ok')
                return redirect(url_for('users.auth_add'))
            except Exception as e:
                print(e)
                flash(message='添加权限失败', category='error')
                return redirect(url_for('users.auth_add'))
    else:
        pass
    return render_template('users/auth_add.html', form=form)


# 编辑权限
@users.route('/auth_edit/<int:id>', methods=['GET', 'POST'])
@login_required
def auth_edit(id=None):
    form = AuthForm()
    auth = Auth.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        auth_count = Auth.query.filter_by(name=data['name']).count()
        if auth.name != data['name'] and auth_count == 1:
            flash(message='该权限已存在，请重新输入', category='error')
            return redirect(url_for('users.auth_edit', id=id))
        else:
            try:
                auth.name = data['name']
                auth.url = data['url']
                db.session.add(auth)
                db.session.commit()
                user = User.query.filter_by(username=session['user']).first_or_404()
                login_log_add(user_id=user.id, operation_type='编辑权限', ip_address=request.remote_addr)
                flash(message='添加权限成功', category='ok')
                return redirect(url_for('users.auth_edit', id=id))
            except Exception as e:
                print(e)
                flash(message='添加权限失败', category='error')
                return redirect(url_for('users.auth_edit', id=id))
    else:
        pass
    return render_template('users/auth_edit.html', form=form, auth=auth)


# 删除权限
@users.route('/auth_delete/<int:id>', methods=['GET'])
@login_required
def auth_delete(id=None):
    auth = Auth.query.filter_by(id=id).first_or_404()
    db.session.delete(auth)
    db.session.commit()
    user = User.query.filter_by(username=session['user']).first()
    login_log_add(user_id=user.id, operation_type='删除权限', ip_address=request.remote_addr)
    flash(message='删除权限成功', category='ok')
    return redirect(url_for('users.auth_list', page=1))


# 操作日志
@users.route('/login_log/<int:page>/', methods=['GET'])
@login_required
def login_log(page=None):
    if page is None:
        page = 1
    page_data = LoginLog.query.order_by(LoginLog.id.desc()).paginate(page=page, per_page=10)
    return render_template('users/login_log.html', page_data=page_data)
