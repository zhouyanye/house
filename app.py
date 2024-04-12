from flask import Flask, render_template, request, redirect
from settings import Config, db
from models import House
from register import user_page
from werkzeug.routing import BaseConverter

app = Flask(__name__)
# 把Config类加到应用程序实例
app.config.from_object(Config)
# 在app.py中初始化数据库
db.init_app(app)
app.config['SECRET_KEY'] = 'house'
# 注册蓝图
app.register_blueprint(user_page, url_prefix='/user_page')

# @app.route('/')
# def index():
#     return render_template('index.html')


# 第二种注册
def index():
    return render_template('index.html')
app.add_url_rule('/', view_func=index)


# 一个视图函数绑定多个url
@app.route('/page')
@app.route('/page/<int:page>')
def pages(page=1):
    return '当前页码是 {}'.format(page)


# 路由传参
@app.route('/list/<int:page>')
def list(page):
    return '当前页码是 {}'.format(page)


# 在地址栏传入
# 在地址栏传入url http://127.0.0.1:5000/list?page=4
# 如何接受get请求中传过来参数
@app.route('/list', methods=['GET'])
def show_list():
    # 接受get请求中传过来的参数
    page_ = request.args.get('page', 1, type=int)  # 默认值为1 类型是int  requset.args.get(key, default, type)
    username = request.args.get('username', )
    return '当前页码是{}'.format(page_) + '当前用户是{}'.format(username)


# post提交表单
# 登陆表单 http://127.0.0.1:5000/login  表单里面传入了username和password
@app.route('/login', methods=['POST'])
def login():
    # 接受post请求中传过来的参数
    username = request.form.get('loginName')  # get request.args.get(key, default, type)
    password = request.form.get('loginpwd')
    return '当前用户名是{} '.format(username) + '当前密码是{}'.format(password) if username and password else '用户名是None 密码是None'


# 自定义转换器
class MoblieConverter(BaseConverter):
    regex = r'1[3-9]\d{9}$'


app.url_map.converters["mobile"] = MoblieConverter


@app.route('/user/<mobile:mobile>')
def send_sms(mobile):
    return f'手机号是{mobile}'


# 头哥
@app.route('/userByName/<string:username>')
def users(username):
    return '用户名为{}'.format(username)


@app.route('/userById/<int:id>')
def userinfo(id):
    return '用户ID为{}'.format(id)



@app.route('/register')
def register():
    return '注册页面'


@app.route('/logout')
def logout():
    return '注销页面'


# 处理请求



# 重定向
@app.route('/redirect')
def redirect_page():
    return redirect('http://www.baidu.com')


# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return '页面不存在404', 404


# 静态文件
@app.route('/static')
def static_page():
    return app.send_static_file('index.html')


# @app.route('/')
# def test():
#     # 查询第一条数据
#     first_user = House.query.first()
#     print(first_user)  # 控制台打印输出
#     return 'ok'  # 网页返回ok


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
