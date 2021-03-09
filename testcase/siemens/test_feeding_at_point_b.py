# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/14 18:50 
  @Auth : 于洋
  @File : test_b.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""

import allure,time,pytest
from basics.carry import Carry_ability
from common.path import *



class  Test_task_B():
    '''A点送料流程'''

    bs = Carry_ability(mysqlname='siemens_mysql',
                          logname='siemens',logpath=logs_dir + r'\siemens.log',
                          testdatas=siemens_yaml)


    @allure.title('任务创建完成')
    # @allure.description('创建任务断言任务状态')
    def test_create(self):
        '''创建任务'''
        self.bs.log.info('---创建任务---')
        self.bs.create_task('b')
        assert self.bs.select_task_status() == '创建'


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
        # self.bs.log.debug('是否检测料架中：{}'.format(s[2][-1]))
        # # 提前到达结果数据库同步慢，导致数据库状态更新，检测料架状态已以后，无法执行该用例
        # assert s[2][-1] == 'intervene'

    @allure.title('检测料架异常')
    def test_docking_abnormal(self):
        '''检测料架异常'''
        self.bs.log.info('---检测料架---')
        s = self.bs.task_status(k=2, v='intervene')
        assert s == True
        # s = self.bs.task_status(k=2, v='intervene')
        # self.bs.log.debug('检测料架状态：{}'.format(s[2][-1]))
        # assert s[2][-1] == 'intervene'

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
        # self.bs.log.debug('人工处理：{}'.format(s[3][-1]))
        # assert s[3][-1] == 'finished'
        assert s == True

    @allure.title('前往卸载点')
    def test_go_unloading(self):
        '''前往卸载点'''
        self.bs.log.info('---前往卸载点---')
        s = self.bs.task_status(k=4, v='processing')
        assert s == True

        # self.bs.log.debug('人工处理：{}'.format(s[4][-1]))
        # assert s[4][-1] == 'processing'

    @allure.title('到达卸载点')
    def test_arrive_unloading(self):
        '''到达卸载点'''
        self.bs.log.info('---到达卸载点---')
        l = self.bs.finish()
        assert l == True
        # s = self.bs.task_status(k=2, v='intervene')
        # self.bs.log.debug('提前到达卸载点：{}'.format(s[4][-1]))
        # assert s[4][-1] == 'finished'

    @allure.title('顶升下降')
    def test_lift_decline(self):
        '''顶升完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=5, v='finished')
        assert s == True

        # self.bs.log.debug('顶升状态：{}'.format(s[5][-1]))
        # assert s[5][-1] == 'finished'

    @allure.title('undocking')
    def test_undocking(self):
        '''undocking'''
        self.bs.log.info('---undocking---')
        s = self.bs.mysql.getstatus(self.bs.transportNo)
        if s[6][-1] == 'finished' or s[6][-1] == 'intervene':
            self.bs.log.debug('undocking状态：{}'.format(s[6][-1]))
            if s[6][-1] == 'finished':
                assert s[6][-1] == 'finished'
            else:
                assert s[6][-1] == 'intervene'
                self.bs.resume()

    @allure.title('带回空料架')
    def test_choice_rack(self):
        '''带回空料架'''
        self.bs.log.info('---带回空料架---')
        f = self.bs.rack_task()
        assert f == True
        # s = self.bs.task_status(k=2, v='intervene')
        # self.bs.log.debug('带回空料架：{}'.format(s[7][-1]))
        # time.sleep(10)
        # f = self.bs.rack_task()
        # self.bs.log.debug('带回空料架结果：{}'.format(f))
        # assert s[7][-1] == 'finished'

    @allure.title('导航前往空料架点')
    def test_empty_rack(self):
        '''导航前往空料架点'''
        self.bs.log.info('---导航和---')
        s = self.bs.task_status(k=9, v='processing')
        assert s == True

        # self.bs.log.debug('导航状态：{}'.format(s[9][-1]))
        # assert s[9][-1] == 'processing'

    @allure.title('到达空料架点')
    def test_arrive_empty_rack(self):
        '''到达空料架点'''
        self.bs.log.info('---到达---')
        f = self.bs.finish()
        assert f == True
        # s = self.bs.task_status(k=2, v='intervene')
        # self.bs.log.debug('到达空料架点：{}'.format(s[9][-1]))
        # assert s[9][-1] == 'finished'

    @allure.title('空料架docking中')
    def test_empty_rack_docking(self):
        '''空料架docking中'''
        s = self.bs.task_status(k=10, v='processing')
        assert s == True
        # self.bs.log.debug('到达空料架点：{}'.format(s[10][-1]))
        # assert s[10][-1] == 'processing'

    @allure.title('空料料架docking异常')
    def test_empty_abnormal(self):
        '''空料料架docking异常'''
        self.bs.log.info('---异常---')
        s = self.bs.task_status(k=10, v='intervene')
        assert s == True

        # s =self.if_taks_status(current_task_status,10,'intervene')
        # self.bs.log.debug('空料料架docking异常：{}'.format(s[10][-1]))
        # assert s[10][-1] == 'intervene'

    @allure.title('空料架异常转人工')
    def test_abnormal_two(self):
        '''空料架异常转人工'''
        self.bs.log.info('---人工---')
        r = self.bs.resume()
        assert r == True

    @allure.title('顶升完成')
    def test_empty_lift(self):
        '''顶升完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=11, v='processing')
        assert s == True

        # self.bs.log.debug('顶升状态：{}'.format(s[11][-1]))
        # assert s[11][-1] == 'finished'

    @allure.title('导航前往空料架卸载点')
    def test_navigation_unloading(self):
        '''导航前往空料架卸载点'''
        self.bs.log.info('---导航---')
        s = self.bs.task_status(k=12, v='processing')
        assert s == True

        # self.bs.log.debug('导航状态：{}'.format(s[12][-1]))
        # assert s[12][-1] == 'processing'

    @allure.title('到达空料架卸载点')
    def test_arrive_empty_unloading(self):
        '''到达空料架卸载点'''
        self.bs.log.info('---到达---')
        t = self.bs.finish()
        assert t == True
        # s = self.bs.task_status(k=2, v='intervene')
        # self.bs.log.debug('到达空料架卸载点：{}'.format(s[12][-1]))
        # assert s[12][-1] == 'finished'

    @allure.title('顶升下载下降完成')
    def test_lift(self):
        '''顶升下载下降完成'''
        self.bs.log.info('---顶升---')
        s = self.bs.task_status(k=13, v='finished')
        assert s == True

        # self.bs.log.debug('顶升状态：{}'.format(s[13][-1]))
        # assert s[13][-1] == 'finished'

    @allure.title('undocking')
    def test_undocking_empry(self):
        '''undocking'''
        self.bs.log.info('---undocking---')
        s = self.bs.mysql.getstatus(self.bs.transportNo)
        if s[14][-1] == 'finished' or s[14][-1] == 'intervene':
            self.bs.log.debug('undocking：{}'.format(s[14][-1]))
            if s[14][-1] == 'finished':
                assert s[14][-1] == 'finished'
            else:
                assert s[14][-1] == 'intervene'
                self.bs.resume()

    @allure.title('任务完成')
    def test_finished(self):
        '''任务完成'''
        self.bs.log.info('---完成---')
        s = self.bs.task_status(k=14, v='finished')
        assert s == True

        # self.bs.log.debug('任务完成')
        # assert s[14][-1] == 'finished'



if __name__ == '__main__':
    pass

