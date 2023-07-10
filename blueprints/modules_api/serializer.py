# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""
from extensions import db
from models import Modules
from utils.flask_serializer.serializer import Serializer


class ModulesSerializer(Serializer):
    db = db
    model = Modules
    fields = "__all__"
