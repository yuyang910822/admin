# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/2 22:58
"""
import os
# 顶层目录
dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例目录
cases_dir = os.path.join(dirs,'testcase')

# 测试报告目录
reports_dir = os.path.join(dirs,'reports')

# 日志目录
logs_dir = os.path.join(dirs,'log')

# 配置文件目录
config_dir = os.path.join(dirs,'config')

# 接口文件目录
api_dir = os.path.join(dirs +r'\config\api_config.yaml')

# 数据库文件目录
mysql_dir = os.path.join(dirs +r'\config\mysql_config.yaml')

# 西门子
siemens_yaml = os.path.join(dirs+r'\data\siemens.yaml')

# 广域铭岛
link_yaml = os.path.join(dirs+r'\data\link.yaml')

# 安捷利
ajl_yaml = os.path.join(dirs+r'\data\ajl.yaml')

# 大连坚山
blue_yaml = os.path.join(dirs+r'\data\blue.yaml')

# 冬奥测试赛
dacs_yaml = os.path.join(dirs,r'\data\blue.yaml')

