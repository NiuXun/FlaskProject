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
    cpu_type = StringField(
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
    memory_capacity = StringField(
        label='内存容量',
        validators=[
            DataRequired(message='请输入内存容量 ！'),
        ],
        description='内存容量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入内存容量',
            # 'required': 'required',
        }
    )
    disk_capacity = StringField(
        label='硬盘容量',
        validators=[
            DataRequired(message='请输入硬盘容量 ！'),
        ],
        description='硬盘容量',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入硬盘容量',
            # 'required': 'required',
        }
    )
    disk_type = SelectField(
        label='硬盘类型',
        validators=[
            DataRequired(message='请输入硬盘类型 ！'),
        ],
        description='硬盘类型',
        coerce=str,
        choices=[('SATA','SATA'),('SAS','SAS'),('SSD','SSD')],
        render_kw={
            'class': 'form-control',
        }
    )
    network_card_type = SelectField(
        label='网卡类型',
        validators=[
            DataRequired(message='请输入网卡类型 ！'),
        ],
        description='网卡类型',
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
    groups = SelectMultipleField(
        label='所属主机组',
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
    device_type = SelectField(
        label='设备类型',
        validators=[
            DataRequired(message='请输入设备类型 ！'),
        ],
        description='设备类型',
        coerce=str,
        choices=[('服务器','服务器'),('网络设备','网络设备'),('存储设备','存储设备')],
        render_kw={
            'class': 'form-control',
        }
    )
    device_model = StringField(
        label='设备型号',
        validators=[
            DataRequired(message='请输入设备型号 ！'),
        ],
        description='设备型号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入设备型号',
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


class IDCForm(FlaskForm):
    name = StringField(
        label='机房名称',
        validators=[
            DataRequired(message='请输入机房名称 ！'),
        ],
        description='机房名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入机房名称',
            # 'required': 'required',
        }
    )
    address = StringField(
        label='机房地址',
        validators=[
            DataRequired(message='请输入机房地址 ！'),
        ],
        description='机房地址',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入机房地址',
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


class TagForm(FlaskForm):
    name = StringField(
        label='标签名称',
        validators=[
            DataRequired(message='请输入标签名称 ！'),
        ],
        description='标签名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入标签名称',
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


class AssetsForm(FlaskForm):
    assets_number = IntegerField(
        label='资产编号',
        validators=[
          DataRequired(message='请输入资产编号！'),
        ],
        description='资产编号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入资产编号',
            # 'required': 'required',
        }
    )
    name = StringField(
        label='资产名称',
        validators=[
            DataRequired(message='请输入资产名称！'),
        ],
        description='资产名称',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入资产名称',
            # 'required': 'required',
        }
    )
    location = StringField(
        label='资产位置',
        validators=[
            DataRequired(message='请输入资产位置！'),
        ],
        description='资产位置',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入资产位置',
            # 'required': 'required',
        }
    )
    use = StringField(
        label='资产用途',
        validators=[
            DataRequired(message='请输入资产用途！'),
        ],
        description='资产用途',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入资产用途',
            # 'required': 'required',
        }
    )
    nature = StringField(
        label='资产性质',
        validators=[
            DataRequired(message='请输入资产性质！'),
        ],
        description='资产性质',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入资产性质',
            # 'required': 'required',
        }
    )
    tags = SelectMultipleField(
        label='标签',
        coerce=int,
        choices=[],
        description='标签',
        render_kw={
            'class': 'form-control col-md-5',
        }
    )
    idc_id = SelectField(
        label='所属机房',
        description='所属机房',
        coerce=int,
        choices=[],
        render_kw={
            'class': 'form-control',
        }
    )
    manage_ip = StringField(
        label='管理IP',
        validators=[
            DataRequired(message='请输入管理IP地址 ！'),
            IPAddress(ipv4=True, message='请输入正确的管理IP地址'),
        ],
        description='管理IP',
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入管理IP地址',
            # 'required': 'required',
        }
    )
    device_type = SelectField(
        label='设备类型',
        description='设备类型',
        coerce=str,
        choices=[('服务器','服务器'),('网络设备','网络设备'),('存储设备','存储设备')],
        render_kw={
            'class': 'form-control',
            'id': 'type',
            'onChange':"type_select();",
        }
    )
    device_status = SelectField(
        label='设备状态',
        description='设备状态',
        coerce=str,
        choices=[('上架', '上架'), ('下架', '下架'), ('未用', '未用')],
        render_kw={
            'class': 'form-control',
        }
    )
    device_name = SelectField(
        label='设备名称',
        description='设备名称',
        coerce=str,
        choices=[],
        render_kw={
            'class': 'form-control',
            'id': 'select_device_name',
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