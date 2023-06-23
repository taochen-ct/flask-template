# coding=utf-8
"""
@Modify Time :2023/3/15 21:11    
@Author      :tao.chen 
"""
from utils.config import Config

config = Config()


class BaseConfig(object):
    """基础配置"""

    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = (
        "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset=utf8".format_map(
            dict(config.get("database"))
        )
    )

    # 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    """开发环境配置"""

    # SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    """测试环境配置"""

    pass


class ProductionConfig(BaseConfig):
    """生产环境(上线环境)配置"""

    pass
