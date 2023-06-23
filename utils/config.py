# coding=utf-8
"""
@Modify Time :2023/6/11 11:28    
@Author      :tao.chen 
"""

import configparser
import os


class Config:
    def __init__(self):
        BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        CONFIG_FILE = os.path.join(BASE_PATH, "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE)

    def get(self, filename, key=None):
        if key is None:
            return self.config.items(filename)
        conf = self.config.get(filename, key)
        return conf

    def path(self):
        BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        return BASE_PATH


if __name__ == "__main__":
    config = Config()
    print(config.get("database"))
