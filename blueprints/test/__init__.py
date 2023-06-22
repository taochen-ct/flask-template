from flask import Blueprint
from . import views
from extensions import register_api

test_bp = Blueprint("test", __name__)
register_api(
    test_bp,
    view=views.UserViewSet,
    endpoint='users',
    url='/api/test/',
    pk='test_id',
    pk_type='int'
)

# user_views = views.UserViewSet.as_view("users")
# test_bp.add_url_rule("/api/test/", defaults={"test_id": None}, view_func=user_views, methods=['GET'])
# test_bp.add_url_rule("/api/test/", view_func=user_views, methods=['POST'])
# test_bp.add_url_rule("/api/test/<int:test_id>", view_func=user_views, methods=['GET', 'DELETE', 'PUT'])
