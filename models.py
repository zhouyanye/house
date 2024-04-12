# 存放数据库模型 数据库表

from settings import db


# house_info
class House(db.Model):
    # 指定表名
    __tablename__ = 'house_info'  # 和数据库的表名一样
    # 语法 字段名=db.Column(数据类型,[选项])
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)    # 指定字段名和类型
    title = db.Column(db.String(100))
    rooms = db.Column(db.String(100))
    area = db.Column(db.String(100))
    price = db.Column(db.String(100))
    direction = db.Column(db.String(100))
    rent_type = db.Column(db.String(100))
    region = db.Column(db.String(100))
    block = db.Column(db.String(100))
    address = db.Column(db.String(200))
    traffic = db.Column(db.String(100))
    publish_time = db.Column(db.Integer)
    facilities = db.Column(db.TEXT)
    highlights = db.Column(db.TEXT)
    matching = db.Column(db.TEXT)
    travel = db.Column(db.TEXT)
    page_views = db.Column(db.Integer)
    landlord = db.Column(db.String(30))
    phone_num = db.Column(db.String(100))
    house_num = db.Column(db.String(100))

    def __repr__(self):
        return "House : %s,%s " % (self.address, self.id)



# house_recommend
class Recommend(db.Model):
    __tablename__ = 'house_recommend'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    house_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    address = db.Column(db.String(100))
    block = db.Column(db.String(100))
    score = db.Column(db.Integer)


# user_info
class User(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    collect_id = db.Column(db.String(250))
    seen_id = db.Column(db.String(250))

    def __repr__(self):
        return "User : %s,%s' " % (self.name, self.password)
