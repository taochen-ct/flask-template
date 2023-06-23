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


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]
