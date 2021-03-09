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
    path: 读取文件路径
    title：文件数据对象标题
    '''
    with open(path, encoding='utf-8') as y:
        data = yaml.load(y, Loader=yaml.FullLoader)
    return data
1



