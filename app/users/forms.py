from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, Regexp


class UserForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            DataRequired(message='请输入用户名 ！'),
            Length(min=4, max=16),
        ],
        description='用户名',
        render_kw={
            'class': 'form-control',
            'id': 'inputUsername',
            'placeholder': '请输入用户名',
            # 'required': 'required',
        }
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='请输入密码 ！'),
            Length(min=4, max=16),
            Regexp(r'^[A-Za-z][A-Za-z0-9]', message='非法字符'),
        ],
        description='密码',
        render_kw={
            'class': 'form-control',
            'id': 'inputPassword',
            'placeholder': '请输入密码',
            # 'required': "required",
        }
    )
    name = StringField(
        label='姓名',
        validators=[
            DataRequired('请输入姓名 ！'),
            Length(max=20),
        ],
        description='姓名',
        render_kw={
            'class': 'form-control',
            'id': 'inputName',
            'placeholder': '请输入姓名',
            # 'required': 'required',
        }
    )
    email = StringField(
        label='邮箱地址',
        validators=[
            DataRequired('请输入邮箱地址 ！'),
            Email('请输入正确的邮箱地址 ！'),
        ],
        description='邮箱地址',
        render_kw={
            'class': 'form-control',
            'id': 'inputEmail',
            'placeholder': '请输入邮箱地址',
            # 'required': 'required',
        }
    )
    phone = StringField(
        label='联系方式',
        validators=[
            DataRequired('请输入联系方式 ！')
        ],
        description='联系方式',
        render_kw={
            'class': 'form-control',
            'id': 'inputPhone',
            'placeholder': '请输入联系方式',
            # 'required': 'required',
        }
    )
    company_name = StringField(
        label='公司名称',
        validators=[
            DataRequired('请输入公司名称 ！'),
        ],
        description='公司名称',
        render_kw={
            'class': 'form-control',
            'id': 'inputCompanyName',
            'placeholder': '请输入公司名称',
            # 'required': 'required',
        }
    )

    is_active = SelectField(
        label='账号状态',
        description='账号状态',
        choices=[('启用', '启用'), ('禁用', '禁用'), ],
        validators=[
            DataRequired(message='请选择账号状态'),
        ],
        render_kw={
            'class': 'form-control',
            'id': 'inputActive',
        }
    )

    is_admin = SelectField(
        label='账号类型',
        description='账号类型',
        choices=[('普通用户', '普通用户'), ('系统管理员', '系统管理员'), ],
        validators=[
            DataRequired(message='请选择账号类型'),
        ],
        render_kw={
            'class': 'form-control',
            'id': 'inputAdmin',
        }
    )

    group = SelectMultipleField(
        label='用户组',
        validators=[
            DataRequired(message='请选择一个选项'),
        ],
        coerce=int,
        choices=[],
        description='用户组',
        render_kw={
            'class': 'form-control col-md-5',
        }
    )

    role = SelectMultipleField(
        label='角色',
        validators=[
            DataRequired(message='请选择一个选项'),
        ],
        coerce=int,
        choices=[],
        description='角色',
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


class GroupForm(FlaskForm):
    name = StringField(
        label='用户组名称',
        validators=[
            DataRequired(message='请输入用户组名称 ！'),
            Length(max=20),
        ],
        description='用户组名称',
        render_kw={
            'class': 'form-control',
            'id': 'inputName',
            'placeholder': '请输入用户组名称',
            # 'required': 'required',
        }
    )
    is_admin = SelectField(
        label='用户组类型',
        description='用户组类型',
        choices=[('普通组', '普通组'), ('管理员组', '管理员组'), ],
        validators=[
            DataRequired(message='请选择用户组类型'),
        ],
        render_kw={
            'class': 'form-control',
            'id': 'inputAdmin',
        }
    )
    roles = SelectMultipleField(
        label='角色列表',
        description='角色列表',
        coerce=int,
        choices=[],
        validators=[
            DataRequired(message='请选择角色'),
        ],
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


class RoleForm(FlaskForm):
    name = StringField(
        label='角色名称',
        validators=[
            DataRequired(message='请输入角色名称 ！'),
            Length(max=20),
        ],
        description='角色名称',
        render_kw={
            'class': 'form-control',
            'id': 'inputName',
            'placeholder': '请输入角色名称',
            # 'required': 'required',
        }
    )
    is_admin = SelectField(
        label='角色类型',
        description='角色类型',
        choices=[('普通角色', '普通角色'), ('管理员角色', '管理员角色'), ],
        validators=[
            DataRequired(message='请选择角色类型'),
        ],
        render_kw={
            'class': 'form-control',
            'id': 'inputAdmin',
        }
    )
    auths = SelectMultipleField(
        label='权限列表',
        description='权限列表',
        coerce=int,
        choices=[],
        validators=[
            DataRequired(message='请选择权限'),
        ],
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


class AuthForm(FlaskForm):
    name = StringField(
        label='权限名称',
        validators=[
            DataRequired('请输入权限名称 ！'),
            Length(max=20),
        ],
        description='权限名称',
        render_kw={
            'class': 'form-control',
            'id': 'inputName',
            'placeholder': '请输入权限名称',
            # 'required': 'required',
        }
    )
    url = StringField(
        label='权限地址',
        validators=[
            DataRequired('请输入权限地址 ！'),
            Length(max=50),
        ],
        description='权限地址',
        render_kw={
            'class': 'form-control',
            'id': 'inputUrl',
            'placeholder': '请输入权限地址',
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