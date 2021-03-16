# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/2/16 22:02 
  @Auth : 于洋
  @File : conftest.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""


import pytest,time

import paramiko
#
# 连接远程服务器进行数据库操作
@pytest.fixture()
def ssh_connect():
    ssh = paramiko.SSHClient()  # 创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname='172.16.5.120', port=22, username='root', password='Forwardx@2020')  # 连接服务器
    yield ssh
    ssh.close()  # 关闭连接