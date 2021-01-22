# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/13 21:10 
  @Auth : 于洋
  @File : get_log.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import logging
from config.path import *
def log():

    # 设置日志收集器
    log = logging.getLogger('py')
    log.setLevel('DEBUG')
    log.handlers.clear()
    # 设置日志处理器
    handler = logging.StreamHandler()
    handler.setLevel('DEBUG')

    f_handler = logging.FileHandler(log_path,mode='a+',encoding='utf-8')
    f_handler.setLevel('DEBUG')


    # 收集器添加处理器
    log.addHandler(handler)
    log.addHandler(f_handler)

    # 设置人日志格式
    # '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')'
    f = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    handler.setFormatter(f)
    f_handler.setFormatter(f)

    return log



if __name__ == '__main__':
    a = log()

