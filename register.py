from flask import Flask, Blueprint, render_template, Response, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

import json
from settings import db
from models import User, House

user_page = Blueprint('user_page', __name__)


class RegisterForm(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired(), Length(min=6, max=15, message='用户名长度必须在6到15个字符之间'),
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名必须以字母开头')])
    password = PasswordField(label='密码', validators=[DataRequired()])
    confirm_password = PasswordField(label='再次输入密码', validators=[DataRequired(), EqualTo('password')])
    email = EmailField(label='邮箱', validators=[DataRequired(), Email(message='邮箱格式不正确')])
    submit = SubmitField('提交')


@user_page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        email = form.email.data
        result = User.query.filter_by(name=name).all()

        if len(result) == 0:
            new_user = User(name=name, password=pwd, email=email)
            db.session.add(new_user)
            db.session.commit()
            json_str = json.dumps({'status': 'success', 'message': f'{new_user.name}注册成功'})
            res = Response(json_str, status=200)
            res.set_cookie('name', new_user.name, 3600 * 2)
            return res
        else:
            json_str = json.dumps({'status': 'fail', 'message': f'{name}已存在'})
            res = Response(json_str, status=200)
            return res

    house_total_num = House.query.count()  # 总房源数
    house_new_list = House.query.order_by(House.publish_time.desc()).limit(6).all()  # 最新房源
    house_hot_list = House.query.order_by(House.page_views.desc()).limit(4).all()  # 最热房源
    return render_template('index.html', form=form, num=house_total_num, house_total_num=house_total_num,
                           house_new_list=house_new_list, house_hot_list=house_hot_list)
