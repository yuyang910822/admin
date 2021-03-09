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


#
@pytest.fixture()
def timesleep():
    time.sleep(2)


    1