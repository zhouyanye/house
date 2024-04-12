# 配置文件
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()  # 用pymysql替换MySQLdb
# 创建SQLAlchemy实例对象
db = SQLAlchemy()


class Config:
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/house'
    # 压制警告SQLAlchemy 的警告信息
    SQLALCHEMY_TRACK_MODIFICATIONS = False
