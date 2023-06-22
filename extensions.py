import pymysql
import sentry_sdk
from werkzeug.routing import BaseConverter
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()


def register_api(blueprint, view, endpoint, url, pk, pk_type):
    """注册蓝图api路由"""

    view_func = view.as_view(endpoint)
    blueprint.add_url_rule(url, defaults={pk: None},
                           view_func=view_func, methods=['GET', ])
    blueprint.add_url_rule(url, view_func=view_func, methods=['POST', ])
    blueprint.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                           methods=['GET', 'PUT', 'DELETE'])


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
