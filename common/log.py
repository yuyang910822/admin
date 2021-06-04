# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/13 21:10 
  @Auth : 于洋
  @File : log.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""

import logging
from logging.handlers import TimedRotatingFileHandler



class Mylog(logging.Logger):

    def __init__(self,name,level='DEBUG',file=None):
        super().__init__(name,level)
        # 日志格式
        fmt = logging.Formatter("%(levelname)s - %(asctime)s - %(filename)s[line:%(lineno)d] : %(message)s")
        # 日志处理器
        p = logging.StreamHandler()
        p.setFormatter(fmt)
        self.addHandler(p)
        # 文件处理器
        if file:
            f = TimedRotatingFileHandler(file, when='D', backupCount=7,encoding='utf-8')
            f.setFormatter(fmt)
            self.addHandler(f)






















































