# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/2/20 16:31 
  @Auth : 于洋
  @File : yaml.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import yaml
from common.path import *

def read_yaml(path):
    '''
    path: 路径
    return：读取的数据
    '''
    with open(path, encoding='utf-8') as y:
        data = yaml.load(y, Loader=yaml.FullLoader)
    return data




