# coding=utf-8
"""
@Modify Time :2023/3/16 22:17    
@Author      :tao.chen 
"""
from abc import ABC


class BaseSerializer(ABC):
    """
    @:param instance
    @:param data
    @:param many
    """

    model = None
    fields = None
    execlude = None
    db = None

    def __init__(self, instance=None, data=None, many=False):
        self.instance = instance
        self.inition_data = data
        self.many = many

        assert any([self.fields is None, not self.execlude]), f"repeated fields and exclude"

        if self.fields == "__all__":
            self.fields = self.model.__fields__

        if self.execlude and isinstance(self.execlude, list):
            self.fields = [i for i in self.model.__fields__ if i not in self.execlude]

    def handle(self, instance):
        """转换json"""

        return {field: getattr(instance, field) for field in self.fields}

    @property
    def data(self):
        if self.instance:
            return self.get_serializer()

    @property
    def valided_data(self):
        return self.is_valid()

    def get_serializer(self):
        """序列化器"""

        # 判断instance是不是实例列表 many参数
        if self.many:
            return [self.handle(i) for i in self.instance]

        # instance为列表，判断many，抛出异常
        if isinstance(self.instance, list):
            raise "please set many = True"

        return self.handle(self.instance)

    def create(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def is_valid(self):
        raise NotImplementedError()


class Serializer(BaseSerializer):
    def is_valid(self):
        return self.inition_data

    def create(self):
        obj = self.model(**self.valided_data)
        return obj

    def save(self, pk=None):
        obj = self.create()
        try:
            self.db.session.add(obj)
            self.db.session.flush()
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise Exception(str(e))

        new_obj = (
            self.db.session.query(self.model)
            .filter_by(**{self.model.__pk__: getattr(obj, self.model.__pk__) if pk is None else pk})
            .first()
        )
        return self.handle(new_obj)

    def update(self):
        try:
            for field in self.instance.__fields__:
                if hasattr(self.instance, field):
                    setattr(self.instance, field, self.valided_data.get(field, getattr(self.instance, field)))
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise Exception(str(e))
        # new_obj = self.db.session.query(self.model).filter_by(id=self.valided_data[self.model.__pk__]).first()
        new_obj = (
            self.db.session.query(self.model)
            .filter_by(**{self.model.__pk__: self.valided_data[self.model.__pk__]})
            .first()
        )
        return self.handle(new_obj)


if __name__ == "__main__":
    from models import User

    user = User()
    test_ser = Serializer(instance=user)
    print(test_ser.data)
