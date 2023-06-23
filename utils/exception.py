# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""
import json


class CustomError(BaseException):
    """自定义错误累"""

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
