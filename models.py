from extensions import db


class User(db.Model):
    """用户表"""
    __tablename__ = "tb_users"  # 指明数据库的表名
    __fields__ = ["id", "name", "email", "password"]

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))


if __name__ == "__main__":
    user = User()
    user.serializer()
