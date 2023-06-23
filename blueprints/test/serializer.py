# coding=utf-8
"""
@Modify Time :2023/3/18 12:09    
@Author      :tao.chen 
"""
from utils.serializer import Serializer
from utils.exception import CustomError
from extensions import db
from models import User


class UserSerializer(Serializer):
    model = User
    fields = "__all__"

    def is_valid(self):
        return self.inition_data

    def create(self):
        obj = self.model(**self.valided_data)
        return obj

    def save(self):
        obj = self.create()
        try:
            db.session.add(obj)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise CustomError(str(e))

        new_obj = db.session.query(User).filter_by(id=obj.id).first()
        return self.handle(new_obj)

    def update(self):
        try:
            for field in self.instance.__fields__:
                if hasattr(self.instance, field):
                    setattr(self.instance, field, self.valided_data.get(field, getattr(self.instance, field)))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise {"data": {"msg": "修改失败", "error": {e}}}
        new_obj = db.session.query(User).filter_by(id=self.valided_data["id"]).first()
        return self.handle(new_obj)
