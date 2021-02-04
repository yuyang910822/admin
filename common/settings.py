# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/2 22:58
"""
import os,time,random,yaml
"""
时间
路径
接口

"""
import requests,json

def gettime():
    '''日期时间'''
    return time.strftime("%Y-%m-%d %H:%M:%S")


def configData():
    y =open(config_config,encoding='utf-8')
    data =yaml.load(y,Loader=yaml.FullLoader)
    y.close()
    return data



homePath= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_config = os.path.join(homePath,'config\configFail.yaml')


def new_id():
    time.sleep(1)
    return time.strftime("%Y%m%d%H%M%S")


if __name__ == '__main__':
    print(get_ye_headers())
