from flask import Blueprint
from flask_restful import Api
from .handler import UserAPI, UserListAPI

test_bp = Blueprint("test", __name__)
api = Api(test_bp)
api.add_resource(UserListAPI, "/test")
api.add_resource(UserAPI, "/test/<test_id>")
