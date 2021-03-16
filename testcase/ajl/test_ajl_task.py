# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/3/15 15:13 
  @Auth : 于洋
  @File : test_ajl_task.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""

import allure,time,pytest
from basics.carry import Carry_ability
from common.path import *

@pytest.mark.usefixtures('ssh_connect')
class Test_ajl():

    bs = Carry_ability(mysqlname='ajl_mysql',
                       logname='ajl', logpath=logs_dir + r'\ajl.log',
                       testdatas=ajl_yaml)


    @allure.title('任务创建完成')
    # @allure.description('创建任务断言任务状态')
    def test_create(self):
        '''创建任务'''
        self.bs.log.info('---创建任务---')
        self.bs.create_task('task_a')
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

    @allure.title('出发')
    def test_docking_in_one(self):
        '''检测料架'''
        self.bs.loadingFinish()
        s = self.bs.task_status(k=2, v='finished')
        assert s == True



    @allure.title('顶升完成')
    def test_lift_rise(self):
        '''顶升完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=3, v='finished')
        assert s == True


    @allure.title('前往卸载点')
    def test_go_unloading(self):
        '''前往卸载点'''
        self.bs.log.info('---前往卸载点---')
        s = self.bs.task_status(k=4, v='processing')
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
        print(55555555555555555555555555555555555555555555555555555)
        s = self.bs.task_status(k=5, v='finished')
        assert s == True


    @allure.title('确认')
    def test_undocking(self):

        self.bs.log.info('---确认---')
        self.bs.receiveMaterials()
        s = self.bs.task_status(k=6, v='finished')
        assert s == True


    @allure.title('任务完成')
    def test_finished(self):
        '''任务完成'''
        self.bs.log.info('---完成---')
        s = self.bs.task_status(k=8, v='finished')
        assert s == True

