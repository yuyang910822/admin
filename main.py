# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/2/20 18:15 
  @Auth : 于洋
  @File : main.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import pytest,os,sys

# pytest.main([ '-s','-v',
#               '--alluredir=allure-results'])



pytest.main([ r'testcase\Standard_one_to_one_manual\ajl\test_ajl_task.py', '-s', '-v'])

# '--reruns=10','--reruns-delay=3',

# os.system('pytest -s -v --alluredir=allure-results')
# os.system('allure generate allure-results -o allure-report -c')
# os.system('allure open allure-report')

