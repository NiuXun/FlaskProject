from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User


class LoginFrom(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[DataRequired(message='请输入用户名 ！')
                    ],
        description='用户名',
        render_kw={
            'class': 'form-username form-control',
            'placeholder': '请输入用户名',
            'id': 'form-username',
            'type': 'text',
            'required': 'required',
        }
    )
    password = PasswordField(
        label='密码',
        validators=[DataRequired(message='请输入密码 ！')
                    ],
        description='密码',
        render_kw={
            'class': 'form-password form-control',
            'placeholder': '请输入密码',
            'type': 'password',
            'id': 'form-password',
            'required': "required",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            'class': 'btn btn-success btn-lg',
            'id': 'login_submit',
        }
    )

    def validate_username(self, field):
        username = field.data
        user = User.query.filter_by(username=username).count()
        if user == 0:
            raise ValidationError('该用户不存在，请重新输入')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        label='旧密码',
        validators=[DataRequired(message='请输入旧密码 ！')
                    ],
        description='旧密码',
        render_kw={
            'class': 'form-password form-control',
            'placeholder': '请输入旧密码',
            # 'required': "required",
        }
    )

    new_password = PasswordField(
        label='新密码',
        validators=[DataRequired(message='请输入新密码！'),
                    ],
        description='新密码',
        render_kw={
            'class': 'form-password form-control',
            'placeholder': '请输入新密码',
            # 'required': "required",
        }
    )
    verify_password = PasswordField(
        label='确认密码',
        validators=[DataRequired(message='请输入确认密码！'),
                    EqualTo(fieldname='new_password', message='两次密码不一致，请重新输入！'),
                    ],
        description='确认密码',
        render_kw={
            'class': 'form-password form-control',
            'placeholder': '请输入确认密码',
            # 'required': "required",
        }
    )
    submit = SubmitField(
        '提交',
        render_kw={
            'class': 'btn btn-success btn-block',
        }
    )

    def validate_old_password(self, filed):
        from flask import session
        old_password = filed.data
        user = User.query.filter_by(username=session['user']).first()
        if not user.check_password(old_password):
            raise ValidationError('旧密码输入错误，请重新输入！')