# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/3/9 15:27
  @Auth : 于洋
  @File : test_empty_rack_back.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import allure,time,pytest
from basics.carry import Carry_ability
from common.path import *


class Test_tack_d():
    '''空料架返回流程'''
    bs = Carry_ability(mysqlname='siemens_mysql',
                       logname='siemens', logpath=logs_dir + r'\siemens.log',
                       testdatas=siemens_yaml)


    @allure.title('任务创建完成')
    # @allure.description('创建任务断言任务状态')
    def test_create(self):
        '''创建任务'''
        self.bs.log.info('---创建任务---')
        self.bs.create_task('d')
        for i in range(1,100):
            s = self.bs.select_task_status()
            if s == '创建':
                assert s == '创建'
                break


    @allure.title('导航前往装载点')
    def test_transit(self):
        '''导航前往装载点'''
        self.bs.log.info('---前往装载点---')
        s =self.bs.task_status(k=1,v='processing')
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
        s = self.bs.task_status(k=2, v='intervene')
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
        s = self.bs.task_status(k=5, v='finished')
        assert s == True

    @allure.title('undocking')
    def test_undocking(self):
        '''undocking'''
        self.bs.log.info('---undocking---')
        s = self.bs.mysql.getstatus(self.bs.transportNo)
        for i in range(1,15):
            time.sleep(1)
            if s[6][-1] == 'finished' or s[6][-1] == 'intervene':
                self.bs.log.debug('undocking状态：{}'.format(s[6][-1]))
                if s[6][-1] == 'finished':
                    assert s[6][-1] == 'finished'
                else:
                    assert s[6][-1] == 'intervene'
                    self.bs.resume()
        self.bs.log.debug(111111111111111)
        return False

    @allure.title('任务完成')
    def test_finished(self):
        '''任务完成'''
        self.bs.log.info('---完成---')
        s = self.bs.task_status(k=6, v='finished')
        assert s == True
