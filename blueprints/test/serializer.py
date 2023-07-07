# coding=utf-8
"""
@Modify Time :2023/3/18 12:09    
@Author      :tao.chen 
"""
from utils.flask_serializer.serializer import Serializer
from extensions import db
from models import User


class UserSerializer(Serializer):
    db = db
    model = User
    fields = "__all__"
