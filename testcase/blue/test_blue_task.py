# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/3/15 15:13 
  @Auth : 于洋
  @File : test_blue_task.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""

import allure,time,pytest
from basics.carry import Carry_ability
from common.path import *


class Test_blue():

    bs = Carry_ability(mysqlname='standard_mysql',
                       logname='blue', logpath=logs_dir + r'\blue.log',
                       testdatas=blue_yaml)



    @allure.title('任务创建完成')
    # @allure.description('创建任务断言任务状态')
    def test_create(self):
        '''创建任务'''
        self.bs.log.info('---创建任务---')
        self.bs.create_task('task_a')
        self.bs.division()
        assert self.bs.select_task_status() == '创建'

    @allure.title('导航前往装载点')
    def test_transit(self):
        '''导航前往装载点'''
        self.bs.log.info('---前往装载点---')
        s = self.bs.task_status(k=1, v='processing')
        assert s == True

    @allure.title('到达装载点')
    def test_loading_one(self):
        '''到达装载点'''
        self.bs.log.info('---到达装载点---')
        f = self.bs.finish()
        assert f == True

    @allure.title('检测料架中')
    def test_docking_in_one(self):
        '''检测料架'''
        s = self.bs.task_status(k=2, v='processing')
        assert s == True

    @allure.title('检测料架异常')
    def test_docking_abnormal(self):
        '''检测料架异常'''
        self.bs.log.info('---检测料架---')
        s = self.bs.task_status(k=2, v='intervene')
        assert s == True

    @allure.title('人工处理')
    def test_abnormal_one(self):
        '''人工处理'''
        self.bs.log.info('---人工处理---')
        l = self.bs.resume()
        assert l == True


    @allure.title('顶升完成')
    def test_lift_rise(self):
        '''顶升完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=3, v='finished')
        assert s == True

    @allure.title('前往停等点')
    def test_go_stop_wait(self):
        self.bs.log.info('---停等点---')
        s = self.bs.task_status(k=4,v='processing')
        assert s == True

    @allure.title('到达停等点')
    def test_arrive_stop_wait(self):
        self.bs.log.info('---到达停等点---')
        s = self.bs.task_status(k=4, v='finished')
        assert s == True

    @allure.title('停等完成')
    def test_stop_wait_complete(self):
        self.bs.log.info('---停等完成---')
        s = self.bs.task_status(k=5, v='finished')
        assert s == True

    @allure.title('前往卸载点')
    def test_go_unloading(self):
        '''前往卸载点'''
        self.bs.log.info('---前往卸载点---')
        s = self.bs.task_status(k=6, v='processing')
        assert s == True


    @allure.title('到达卸载点')
    def test_arrive_unloading(self):
        '''到达卸载点'''
        self.bs.log.info('---到达卸载点---')
        l = self.bs.finish()
        assert l == True


    @allure.title('顶升下降')
    def test_lift_decline(self):
        '''顶升完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=7, v='finished')
        assert s == True

    @allure.title('undocking')
    def test_undocking(self):
        '''undocking'''
        self.bs.log.info('---undocking---')
        s = self.bs.docking(k=8)
        assert s == True

    @allure.title('任务完成')
    def test_finished(self):
        '''任务完成'''
        self.bs.log.info('---完成---')
        s = self.bs.task_status(k=10, v='finished')
        assert s == True


