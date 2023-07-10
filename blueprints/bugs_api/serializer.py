# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""
from extensions import db
from models import Bugs
from utils.flask_serializer.serializer import Serializer


class BugsSerializer(Serializer):
    db = db
    model = Bugs
    fields = "__all__"
