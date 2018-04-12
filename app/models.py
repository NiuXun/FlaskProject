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


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=64), unique=True, nullable=False)
    password = db.Column(db.String(length=256), unique=True, nullable=False)
    name = db.Column(db.String(length=128))
    email = db.Column(db.String(length=128), unique=True)
    phone = db.Column(db.String(length=11), unique=True)
    company_name = db.Column(db.String(length=255), nullable=True)
    groups = db.relationship('Group', secondary=users_groups, backref=db.backref('users', lazy='dynamic'))
    roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
    loginlogs = db.relationship('LoginLog', backref=db.backref('users'))
    is_active = db.Column(db.String(length=32))
    is_admin = db.Column(db.String(length=32))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.username

    @staticmethod
    def create_super_user(username, password):
        from werkzeug.security import generate_password_hash
        user_count = User.query.filter_by(username='admin').count()
        if user_count == 0:
            user = User(
                username=username,
                password=generate_password_hash(password),
                name='超级管理员',
                email='',
                phone='',
                company_name='',
                is_active='有效',
                is_admin='系统管理员',
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark='',
            )
            db.session.add(user)
            db.session.commit()

    # 校验密码
    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


# 角色表
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64), nullable=False)
    is_admin = db.Column(db.String(length=32))
    auths = db.relationship('Auth', secondary=roles_auths, backref=db.backref('roles', lazy='dynamic'))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_modify_time = db.Column(db.DateTime)
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


# 权限表
class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64), unique=True, nullable=False)
    url = db.Column(db.String(length=128), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_modify_time = db.Column(db.DateTime)
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


# 用户组表
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=64), nullable=False)
    roles = db.relationship('Role', secondary=groups_roles, backref=db.backref('groups', lazy='dynamic'))
    is_admin = db.Column(db.String(length=32))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_modify_time = db.Column(db.DateTime)
    description = db.Column(db.String(length=255), nullable=True)

    def __repr__(self):
        return self.name


# 操作日志表
class LoginLog(db.Model):
    __tablename__ = 'loginlog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    operation_type = db.Column(db.String(length=32))
    ip = db.Column(db.String(length=128))
    create_time = db.Column(db.DateTime)

    def __repr__(self):
        return self.ip


# 服务器表
class Server(db.Model):
    __tablename__ = 'server'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sn_number = db.Column(db.String(length=256), nullable=False)
    name = db.Column(db.String(length=64), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    system_version = db.Column(db.String(length=128))
    ip_address = db.Column(db.String(length=256))
    mac_address = db.Column(db.String(length=256))
    RAID_type = db.Column(db.String(length=32))
    cpu_type = db.Column(db.String(length=64))
    cpu_count = db.Column(db.SmallInteger)
    memory_capacity = db.Column(db.String(length=32))
    disk_type = db.Column(db.String(16))
    disk_capacity = db.Column(db.String(length=32))
    network_card_type = db.Column(db.String(length=64))
    network_card_count = db.Column(db.Integer)
    power_count = db.Column(db.SmallInteger)
    groups = db.relationship('HostGroup', secondary=hostgroups_servers, backref=db.backref('servers', lazy='dynamic'))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)
    # server和asset一对一关联
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))

    def __repr__(self):
        return self.name


# 网络设备表
class Network_Device(db.Model):
    __tablename__ = 'network_device'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    sn_number = db.Column(db.String(length=128), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    port_count = db.Column(db.SmallInteger)
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)
    # network_device和asset一对一关联
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))

    def __repr__(self):
        return self.name


# 存储设备表
class Storage(db.Model):
    __tablename__ = 'storage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    sn_number = db.Column(db.String(length=128), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    amount = db.Column(db.String(length=32))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)
    # storage和asset一对一关联
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'))

    def __repr__(self):
        return self.name


# 主机组表
class HostGroup(db.Model):
    __tablename__ = 'host_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    group_use = db.Column(db.String(length=256), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


# 机房表
class IDC(db.Model):
    __tablename__ = 'IDC'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    address = db.Column(db.String(length=256))
    assets_id = db.Column(db.Integer, db.ForeignKey('assets.id'))
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


# 资产表
class Assets(db.Model):
    __tablename__ = 'assets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assets_number = db.Column(db.Integer, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    location = db.Column(db.String(length=128))
    use = db.Column(db.String(length=128))
    nature = db.Column(db.String(length=128))
    tags = db.relationship('Tag', secondary=assets_tags, backref=db.backref('assets', lazy='dynamic'))
    idc_id = db.relationship('IDC', backref=db.backref('assets'))
    manage_ip = db.Column(db.String(length=256))
    device_status = db.Column(db.String(length=32))
    device_type = db.Column(db.String(length=32))
    create_time = db.Column(db.DateTime, default=datetime.now())
    last_modify_time = db.Column(db.DateTime, default=datetime.now())
    remark = db.Column(db.String(length=256), nullable=True)

    servers = db.relationship('Server', backref=db.backref('assets', uselist=False))
    network_devices = db.relationship('Network_Device', backref=db.backref('assets', uselist=False))
    storages = db.relationship('Storage', backref=db.backref('assets', uselist=False))

    def __repr__(self):
        return self.name


# 标签表
class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return self.name


# 设备基本信息表
class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=128), nullable=False)
    device_type = db.Column(db.String(length=64), nullable=False)
    device_model = db.Column(db.String(length=256), nullable=False)
    servers = db.relationship('Server', backref=db.backref('vendors'))
    create_time = db.Column(db.DateTime, default=datetime.now())
    last_modify_time = db.Column(db.DateTime)
    remark = db.Column(db.String(length=256), nullable=True)

    def __repr__(self):
        return  '%r | %r | %r' % (self.name, self.device_type, self.device_model)