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

assets_tags = db.Table('assets_tags',
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                       db.Column('assets_id', db.Integer, db.ForeignKey('assets.id')),
                       )

hostgroups_servers = db.Table('hostgroups_servers',
                              db.Column('host_group_id', db.Integer, db.ForeignKey('host_group.id')),
                              db.Column('server_id', db.Integer, db.ForeignKey('server.id')),
                              )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    addtime = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    remark = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.username

    @staticmethod
    def create_super_user(username, password):
        from werkzeug.security import generate_password_hash
        if User.query.filter_by(username='admin').count() == 0:
            user = User(
                username=username,
                password=generate_password_hash(password),
                name='超级管理员',
                email='',
                phone='',
                company_name='',
                is_active='有效',
                is_admin='系统管理员',
                remark='',
            )
            db.session.add(user)
            db.session.commit()

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64))
    is_admin = db.Column(db.String(length=32))
    auths = db.relationship('Auth', secondary=roles_auths, backref=db.backref('roles', lazy='dynamic'))
    addtime = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64), unique=True)
    url = db.Column(db.String(length=128), unique=True)
    addtime = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64))
    roles = db.relationship('Role', secondary=groups_roles, backref=db.backref('groups', lazy='dynamic'))
    is_admin = db.Column(db.String(length=32))
    addtime = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


class LoginLog(db.Model):
    __tablename__ = 'loginlog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    operation_type = db.Column(db.String(length=32))
    ip = db.Column(db.String(length=128))
    addtime = db.Column(db.DateTime)

    def __repr__(self):
        return self.ip


class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sn_number = db.Column(db.String(length=256))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    device_model_id = db.Column(db.Integer, db.ForeignKey('device_model.id'))
    name = db.Column(db.String(length=64))
    cpu_name = db.Column(db.String(length=32))
    cpu_count = db.Column(db.SmallInteger)
    memory = db.Column(db.String(length=32))
    memory_count = db.Column(db.SmallInteger)
    disk = db.Column(db.String(length=32))
    disk_count = db.Column(db.SmallInteger)
    RAID_type = db.Column(db.String(length=32))
    network_card_type = db.Column(db.String(length=32))
    network_card_count = db.Column(db.Integer)
    power_count = db.Column(db.SmallInteger)
    ip_address = db.Column(db.String(length=256))
    mac_address = db.Column(db.String(length=256))
    system_version = db.Column(db.String(length=128))
    groups = db.relationship('HostGroup', secondary=hostgroups_servers, backref=db.backref('servers', lazy='dynamic'))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


class HostGroup(db.Model):
    __tablename__ = 'host_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


class IDC(db.Model):
    __tablename__ = 'IDC'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(256))
    assets_id = db.Column(db.Integer, db.ForeignKey('assets.id'))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


class Assets(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64))
    assets_number = db.Column(db.Integer)
    location = db.Column(db.String(length=64))
    use = db.Column(db.String(length=64))
    nature = db.Column(db.String(length=32))
    tags = db.relationship('Tag', secondary=assets_tags, backref=db.backref('assets', lazy='dynamic'))
    idcs_id = db.relationship('IDC', backref=db.backref('assets'))
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))
    servers = db.relationship('Server', backref=db.backref('assets', uselist=False))
    create_time = db.Column(db.DateTime, default=datetime.now())
    last_modify_time = db.Column(db.DateTime, default=datetime.now())
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(256))
    servers = db.relationship('Server', backref=db.backref('vendors'))
    models = db.relationship('DeviceModel', backref=db.backref('vendors'))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name

class DeviceModel(db.Model):
    __tablename__ = 'device_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    servers = db.relationship('Server', backref=db.backref('models'))
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name