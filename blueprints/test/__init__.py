from flask import Blueprint
from flask_restful import Api
from .handler import UserApi, UserListApi

test_bp = Blueprint("test", __name__)
api = Api(test_bp)
api.add_resource(UserListApi, "/test")
api.add_resource(UserApi, "/test/<test_id>")
