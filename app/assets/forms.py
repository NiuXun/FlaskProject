from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, IPAddress, MacAddress, NumberRange, Regexp


class ServerForm(FlaskForm):
    sn_number = StringField(
        label='S/N编号',
        validators=[
            DataRequired(message='请输入S/N编号 ！'),
            Regexp(r'^[A-Za-z0-9][A-Za-z0-9]', message='非法字符')
        ],
        description='S/N编号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入S/N编号',
            # 'required': 'required',
        }
    )
    vendor = SelectField(
        label='设备厂商',
        validators=[
            DataRequired(message='请输入设备厂商 ！'),
        ],
        description='设备厂商',
        coerce=int,
        choices=[],
        render_kw={
            'class': 'form-control',
        }
    )
    device_model = SelectField(
        label='设备型号',
        validators=[
            DataRequired(message='请输入设备型号 ！'),
        ],
        description='设备型号',
        coerce=int,
        choices=[],
        render_kw={
            'class': 'form-control',
        }
    )
    name = StringField(
        label='设备名称',
        validators=[
            DataRequired(message='请输入设备名称 ！'),
        ],
        description='设备名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入设备名称',
            # 'required': 'required',
        }
    )
    cpu_name = StringField(
        label='CPU型号',
        validators=[
            DataRequired(message='请输入CPU型号 ！'),
        ],
        description='CPU型号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入CPU型号',
            # 'required': 'required',
        }
    )
    cpu_count = IntegerField(
        label='CPU数量(个)',
        validators=[
            DataRequired(message='请输入CPU数量 ！'),
            NumberRange(min=1, max=32, message='请输入正确的CPU数量'),
        ],
        description='CPU数量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入CPU数量',
            # 'required': 'required',
        }
    )
    memory = StringField(
        label='内存总量',
        validators=[
            DataRequired(message='请输入内存总量 ！'),
        ],
        description='内存总量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入内存总量',
            # 'required': 'required',
        }
    )
    memory_count = IntegerField(
        label='内存数量(个)',
        validators=[
            DataRequired(message='请输入内存数量 ！'),
            NumberRange(min=1, max=64, message='请输入正确的内存数量'),
        ],
        description='内存数量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入内存数量',
            # 'required': 'required',
        }
    )
    disk = StringField(
        label='硬盘总量',
        validators=[
            DataRequired(message='请输入硬盘总量 ！'),
        ],
        description='硬盘总量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入硬盘总量',
            # 'required': 'required',
        }
    )
    disk_count = IntegerField(
        label='硬盘数量(块)',
        validators=[
            DataRequired(message='请输入硬盘数量 ！'),
            NumberRange(min=1, max=64, message='请输入正确的硬盘数量'),
        ],
        description='硬盘数量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入硬盘数量',
            # 'required': 'required',
        }
    )
    RAID_type = SelectMultipleField(
        label='RAID类型',
        validators=[
            DataRequired(message='请选择RAID类型'),
        ],
        coerce=str,
        choices=[('RAID-0', 'RAID-0'), ('RAID-1', 'RAID-1'), ('RAID-5', 'RAID-5')],
        description='RAID类型',
        render_kw={
            'class': 'form-control col-md-5',
        }
    )
    network_card_type = SelectField(
        label='设备型号',
        validators=[
            DataRequired(message='请输入设备型号 ！'),
        ],
        description='设备型号',
        choices=[('万兆', '万兆'), ('千兆', '千兆'), ('百兆', '百兆'), ],
        render_kw={
            'class': 'form-control',
        }
    )
    network_card_count = IntegerField(
        label='网卡数量(个)',
        validators=[
            DataRequired(message='请输入网卡数量 ！'),
            NumberRange(min=1, max=64, message='请输入正确的网卡数量'),
        ],
        description='网卡数量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入网卡数量',
            # 'required': 'required',
        }
    )
    power_count = IntegerField(
        label='电源数量(个)',
        validators=[
            DataRequired(message='请输入电源数量 ！'),
            NumberRange(min=1, max=32, message='请输入正确的电源数量'),
        ],
        description='电源数量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入电源数量',
            # 'required': 'required',
        }
    )
    ip_address = StringField(
        label='IP地址',
        validators=[
            DataRequired(message='请输入IP地址 ！'),
            IPAddress(ipv4=True, message='请输入正确的IP地址'),
        ],
        description='IP地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入IP地址',
            # 'required': 'required',
        }
    )
    mac_address = StringField(
        label='MAC地址',
        validators=[
            DataRequired(message='请输入MAC地址 ！'),
            MacAddress(message='请输入正确的MAC地址'),
        ],
        description='MAC地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入MAC地址',
            # 'required': 'required',
        }
    )
    system_version = StringField(
        label='操作系统版本',
        validators=[
            DataRequired(message='请输入操作系统版本 ！'),
        ],
        description='操作系统版本',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入操作系统版本',
            # 'required': 'required',
        }
    )
    groups = SelectMultipleField(
        label='所属主机组',
        validators=[
            # DataRequired(message='请选择所属主机组'),
        ],
        coerce=int,
        choices=[],
        description='所属主机组',
        render_kw={
            'class': 'form-control col-md-5',
        }
    )
    remark = TextAreaField(
        label='备注',
        description='备注',
        render_kw={
            'class': 'form-control',
            'id': 'inputRemark',
            'rows': 5,
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            'class': 'btn btn-success btn-block',
        }
    )


class VendorForm(FlaskForm):
    name = StringField(
        label='厂商名称',
        validators=[
            DataRequired(message='请输入厂商名称 ！'),
        ],
        description='厂商名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入厂商名称',
            # 'required': 'required',
        }
    )
    address = StringField(
        label='供应商地址',
        validators=[
            DataRequired(message='请输入供应商地址 ！'),
        ],
        description='供应商地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入供应商地址',
            # 'required': 'required',
        }
    )
    remark = TextAreaField(
        label='备注',
        description='备注',
        render_kw={
            'class': 'form-control',
            'id': 'inputRemark',
            'rows': 5,
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            'class': 'btn btn-success btn-block',
        }
    )


class DeviceModelForm(FlaskForm):
    name = StringField(
        label='设备型号',
        validators=[
            DataRequired(message='请输入设备型号 ！'),
        ],
        description='设备型号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入设备型号',
            # 'required': 'required',
        }
    )
    vendor = SelectField(
        label='供应商',
        validators=[
            DataRequired(message='请输入供应商 ！'),
        ],
        description='供应商',
        coerce=int,
        choices=[],
        render_kw={
            'class': 'form-control',
        }
    )
    device_type = SelectField(
        label='设备类型',
        validators=[
            DataRequired(message='请输入设备类型 ！'),
        ],
        description='设备类型',
        coerce=str,
        choices=[('机架式服务器', '机架式服务器'), ('刀片式服务器', '刀片式服务器'), ('塔式服务器', '塔式服务器')],
        render_kw={
            'class': 'form-control',
        }
    )
    remark = TextAreaField(
        label='备注',
        description='备注',
        render_kw={
            'class': 'form-control',
            'id': 'inputRemark',
            'rows': 5,
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            'class': 'btn btn-success btn-block',
        }
    )


class HostGroupForm(FlaskForm):
    name = StringField(
        label='主机组名称',
        validators=[
            DataRequired(message='请输入主机组名称 ！'),
        ],
        description='主机组名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入主机组名称',
            # 'required': 'required',
        }
    )
    remark = TextAreaField(
        label='备注',
        description='备注',
        render_kw={
            'class': 'form-control',
            'id': 'inputRemark',
            'rows': 5,
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            'class': 'btn btn-success btn-block',
        }
    )
