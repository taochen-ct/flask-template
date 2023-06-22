# coding=utf-8
"""
@Modify Time :2023/3/16 22:17    
@Author      :tao.chen 
"""
# flask Marshmallow 序列化/反序列化的
from abc import ABC


class Serializer(ABC):
    """
    序列化类
    @params instance 数据库
    @params data 前端请求
    @many  单条/多条
    """
    model = None
    fields = None
    execlude = None

    def __init__(self, instance=None, data=None, many=False):
        self.instance = instance
        self.inition_data = data
        self.many = many

        assert any([self.fields is None, not self.execlude]), \
            f"repeated fields and exclude"

        if self.fields == "__all__":
            self.fields = self.model.__fields__

        if self.execlude and isinstance(self.execlude, list):
            self.fields = [i for i in self.model.__fields__ if i not in self.execlude]

    def handle(self, instance):
        """转换json"""

        return {
            field: getattr(instance, field)
            for field in self.fields
        }

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
            return [
                self.handle(i)
                for i in self.instance
            ]

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


if __name__ == "__main__":
    from models import User

    user = User()
    test_ser = Serializer(instance=user)
    print(test_ser.data)
