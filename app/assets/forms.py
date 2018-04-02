from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, IPAddress, MacAddress, NumberRange,Regexp


class ServerForm(FlaskForm):
    sn_number = StringField(
        label='S/N编号',
        validators=[
            DataRequired(message='请输入S/N编号 ！'),
            Regexp(r'^[A-Za-z][A-Za-z0-9]', message='非法字符')
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
        label='CPU个数',
        validators=[
            DataRequired(message='请输入CPU个数 ！'),
            NumberRange(min=1,max=32,message='请输入正确的CPU个数'),
        ],
        description='CPU个数',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入CPU个数',
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
        label='内存条个数',
        validators=[
            DataRequired(message='请输入内存条个数 ！'),
            NumberRange(min=1, max=64, message='请输入正确的内存条个数'),
        ],
        description='内存条个数',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入内存条个数',
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
        label='硬盘个数',
        validators=[
            DataRequired(message='请输入硬盘个数 ！'),
            NumberRange(min=1, max=64, message='请输入正确的硬盘个数'),
        ],
        description='硬盘个数',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入硬盘个数',
            # 'required': 'required',
        }
    )
    RAID_type = SelectMultipleField(
        label='RAID类型',
        validators=[
            DataRequired(message='请选择RAID类型'),
        ],
        coerce=str,
        choices=[('RAID-0','RAID-0'),('RAID-1','RAID-1'),('RAID-5','RAID-5')],
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
        choices=[('万兆','万兆'),('千兆','千兆'),('百兆','百兆'),],
        render_kw={
            'class': 'form-control',
        }
    )
    network_card_count = IntegerField(
        label='网卡个数',
        validators=[
            DataRequired(message='请输入网卡个数 ！'),
            NumberRange(min=1, max=64, message='请输入正确的网卡个数'),
        ],
        description='网卡个数',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入网卡个数',
            # 'required': 'required',
        }
    )
    power_count = IntegerField(
        label='电源个数',
        validators=[
            DataRequired(message='请输入电源个数 ！'),
            NumberRange(min=1, max=32, message='请输入正确的电源个数'),
        ],
        description='电源个数',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入电源个数',
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
            DataRequired(message='请选择所属主机组'),
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
    vendor = SelectField(
        label='供应商名称',
        validators=[
            DataRequired(message='请输入供应商名称 ！'),
        ],
        description='供应商名称',
        choices=[],
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