# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""

from flask import Blueprint
from flask_restful import Api
from .handler import ModuleAPI, ModuleListAPI

modules_bp = Blueprint("modules", __name__)
api = Api(modules_bp)
api.add_resource(ModuleListAPI, "/api/module")
api.add_resource(ModuleAPI, "/api/module/<module_uid>")
