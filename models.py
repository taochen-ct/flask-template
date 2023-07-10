from extensions import db


class User(db.Model):
    """用户表"""

    __tablename__ = "tb_users"  # 指明数据库的表名
    __fields__ = ["id", "name", "email", "password"]
    __pk__ = "id"

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置为自增主键
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))


class Modules(db.Model):
    __tablename__ = "tb_modules"  # 指明数据库的表名
    __fields__ = ["uid", "name", "create_time", "modify_time"]
    __pk__ = "uid"

    uid = db.Column(db.String(256), primary_key=True, unique=True)
    name = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.String(30), nullable=False)
    modify_time = db.Column(db.String(30), nullable=False)


class Bugs(db.Model):
    __tablename__ = "tb_bugs"  # 指明数据库的表名
    __fields__ = ["uid", "name", "create_time", "modify_time", "module_uid"]
    __pk__ = "uid"

    uid = db.Column(db.String(256), primary_key=True, unique=True)
    name = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.String(30), nullable=False)
    modify_time = db.Column(db.String(30), nullable=False)
    module_uid = db.Column(db.String(256))


if __name__ == "__main__":
    user = User()
    user.serializer()
