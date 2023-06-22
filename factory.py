from flask import Flask
import settings
from extensions import db, cors, RegexConverter, migrate
from blueprints.test import test_bp
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def create_app():
    """创建APP"""

    app = Flask(__name__)

    # 加载配置
    app.config.from_object(settings.DevelopmentConfig)

    # 错误捕获
    sentry_sdk.init(
        dsn="https://422fe15864c34f549f6b1c4500764edb@o4504852704788480.ingest.sentry.io/4504852708327424",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0
    )

    # 注册蓝图
    app.register_blueprint(test_bp)

    # 初始化扩展
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    app.url_map.converters['regex'] = RegexConverter

    return app
