# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""

from flask import Blueprint
from flask_restful import Api
from .handler import BugAPI, BugListAPI

bugs_bp = Blueprint("bugs", __name__)
api = Api(bugs_bp)
api.add_resource(BugListAPI, "/api/bug")
api.add_resource(BugAPI, "/api/bug/<bug_uid>")
