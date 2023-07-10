from flask import Flask
import settings
from extensions import db, cors, RegexConverter, migrate
from blueprints.test import test_bp
from blueprints.bugs_api import bugs_bp
from blueprints.modules_api import modules_bp
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def create_app():
    """创建APP"""

    app = Flask(__name__)

    # 加载配置
    app.config.from_object(settings.DevelopmentConfig)

    # 错误捕获
    """
    sentry_sdk.init(
            dsn="your_dsn",
            integrations=[FlaskIntegration()],
            traces_sample_rate=1.0
        )
    """

    # 注册蓝图
    blue_prints = [test_bp, bugs_bp, modules_bp]
    for bp in blue_prints:
        app.register_blueprint(bp)
    # app.register_blueprint(test_bp)
    # app.register_blueprint(bugs_bp)
    # app.register_blueprint(modules_bp)

    # 初始化扩展
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    app.url_map.converters["regex"] = RegexConverter

    return app
