from app import db
from datetime import datetime

users_groups = db.Table('users_groups',
                        db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                        )

roles_auths = db.Table('roles_auths',
                       db.Column('auth_id', db.Integer, db.ForeignKey('auth.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                       )

users_roles = db.Table('users_roles',
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       )

groups_roles = db.Table('groups_roles',
                        db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
                        db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
                        )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=64), unique=True)
    password = db.Column(db.String(length=256), unique=True)
    name = db.Column(db.String(length=128))
    email = db.Column(db.String(length=128), unique=True)
    phone = db.Column(db.String(length=11), unique=True)
    company_name = db.Column(db.String(length=255), nullable=True)
    groups = db.relationship('Group', secondary=users_groups, backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
    loginlogs = db.relationship('LoginLog', backref=db.backref('users'))
    is_active = db.Column(db.String(length=32))
    is_admin = db.Column(db.String(length=32))
    addtime = db.Column(db.DateTime, default=datetime.now())
    remark = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.username

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=64))
    is_admin = db.Column(db.String(length=32))
    auths = db.relationship('Auth', secondary=roles_auths, backref=db.backref('roles', lazy='dynamic'))
    addtime = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=64), unique=True)
    url = db.Column(db.String(length=128), unique=True)
    addtime = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=64))
    roles = db.relationship('Role', secondary=groups_roles, backref=db.backref('groups', lazy='dynamic'))
    is_admin = db.Column(db.String(length=32))
    addtime = db.Column(db.DateTime, default=datetime.now())
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class LoginLog(db.Model):
    __tablename__ = 'loginlog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    operation_type = db.Column(db.String(length=32))
    ip = db.Column(db.String(length=128))
    addtime = db.Column(db.DateTime, default=datetime.now())
