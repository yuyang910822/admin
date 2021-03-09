# # -*- coding: utf-8 -*-
# """
# -------------------------------------------------
#   @Time : 2021/1/14 18:50
#   @Auth : 于洋
#   @File : test_b.py
#   @IDE  : PyCharm
#   @Motto: ABC(Always Be Coding)
# -------------------------------------------------
# """
#
# import allure, time
# from basics.business import Business_ability
# from common.path import *
#
#
# class Te77st_task_B(Busines_ability):
#     '''A点送料流程'''
#
#     bs = Business_ability(mysqlname='siemens_mysql', mylogpath=logs_dir)
#
#     @allure.title('任务创建')
#     @allure.description('创建任务断言任务状态')
#     def test_create(self):
#         '''创建任务'''
#
#         self.bs.create_task('b')
#         assert self.bs.select_task_status() == '创建'
#
#     @allure.title('正在前往装载点')
#     def test_transit(self):
#         '''导航前往装载点'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('前往上料点任务状态：{}'.format(s))
#         assert s[1][-1] == 'processing'
#
#     @allure.title('到达装载点')
#     def test_loading_one(self):
#         '''到达装载点'''
#         f = self.bs.finish()
#         self.bs.log.error('提前到达结果'.format(f))
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('是否到达上料点：{}'.format(s))
#         assert s[1][-1] == 'finished'
#
#     @allure.title('检测料架中')
#     def test_docking_in_one(self):
#         '''检测料架'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('是否检测料架中：{}'.format(s))
#         assert s[2][-1] == 'processing'
#
#     @allure.title('检测料架异常')
#     def test_docking_abnormal(self):
#         '''检测料架异常'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('是否检测料架异常：{}'.format(s))
#         assert s[2][-1] == 'intervene'
#
#     @allure.title('人工处理')
#     def test_abnormal_one(self):
#         '''人工处理'''
#         l = self.bs.resume()
#         self.bs.log.error('人工处理结果：'.format(l))
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('人工处理完成：{}'.format(s))
#         assert s[3][-1] == 'finished'
#
#     @allure.title('顶升完成')
#     def test_lift_rise(self):
#         '''顶升完成'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('人工处理完成：{}'.format(s))
#         assert s[3][-1] == 'finished'
#
#     @allure.title('前往卸载点')
#     def test_go_unloading(self):
#         '''前往卸载点'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('人工处理完成：{}'.format(s))
#         assert s[4][-1] == 'processing'
#
#     @allure.title('到达卸载点')
#     def test_arrive_unloading(self):
#         '''到达卸载点'''
#         l = self.bs.finish()
#         self.bs.log.debug('提前到达结果:{}'.format(l))
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('提前到达卸载点：{}'.format(s))
#         assert s[4][-1] == 'finished'
#
#     @allure.title('顶升完成')
#     def test_lift_decline(self):
#         '''顶升完成'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('顶升完成：{}'.format(s))
#         assert s[5][-1] == 'finished'
#
#     @allure.title('undocking')
#     def test_undocking(self):
#         '''undocking'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         if s[6][-1] == 'finished' or s[6][-1] == 'intervene':
#             self.bs.log.debug('undocking完成：{}'.format(s))
#             assert True
#         assert False
#
#     @allure.title('带回空料架')
#     def test_choice_rack(self):
#         '''带回空料架'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('带回空料架：{}'.format(s))
#         time.sleep(10)
#         f = self.bs.rack_task()
#         self.bs.log.debug('带回空料架结果：{}'.format(f))
#         assert s[7][-1] == 'finished'
#
#     @allure.title('导航前往空料架点')
#     def test_empty_rack(self):
#         '''导航前往空料架点'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('导航前往空料架点：{}'.format(s))
#         assert s[9][-1] == 'processing'
#
#     @allure.title('到达空料架点')
#     def test_arrive_empty_rack(self):
#         '''到达空料架点'''
#         time.sleep(5)
#         f = self.bs.finish()
#         self.bs.log.error(f)
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('到达空料架点：{}'.format(s))
#         assert s[9][-1] == 'finished'
#
#     @allure.title('空料架docking中')
#     def test_empty_rack_docking(self):
#         '''空料架docking中'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('到达空料架点：{}'.format(s))
#         assert s[10][-1] == 'processing'
#
#     @allure.title('空料料架docking异常')
#     def test_empty_abnormal(self):
#         '''空料料架docking异常'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         # s =self.if_taks_status(current_task_status,10,'intervene')
#         self.bs.log.debug('空料料架docking异常：{}'.format(s))
#         assert s[10][-1] == 'intervene'
#
#     @allure.title('空料架异常转人工')
#     def test_abnormal_two(self):
#         '''空料架异常转人工'''
#         self.bs.resume()
#         time.sleep(10)
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('空料架异常转人工：{}'.format(s))
#         assert s[10][-1] == 'finished'
#
#     @allure.title('顶升完成')
#     def test_empty_lift(self):
#         '''顶升完成'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('顶升完成：{}'.format(s))
#         assert s[11][-1] == 'finished'
#
#     @allure.title('导航前往空料架卸载点')
#     def test_navigation_unloading(self):
#         '''导航前往空料架卸载点'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('导航前往空料架卸载点：{}'.format(s))
#         assert s[12][-1] == 'processing'
#
#     @allure.title('到达空料架卸载点')
#     def test_arrive_empty_unloading(self):
#         '''到达空料架卸载点'''
#         self.bs.finish()
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('到达空料架卸载点：{}'.format(s))
#         assert s[12][-1] == 'finished'
#
#     @allure.title('顶升下载下降完成')
#     def test_lift(self):
#         '''顶升下载下降完成'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('顶升下载下降完成：{}'.format(s))
#         assert s[13][-1] == 'finished'
#
#     @allure.title('undocking')
#     def test_undocking_empry(self):
#         '''undocking'''
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         if s[14][-1] == 'finished' or s[14][-1] == 'intervene':
#
#             self.bs.log.debug('undocking：{}'.format(s))
#             assert True
#         else:
#             self.bs.log.debug('undocking：{}'.format(s))
#             assert False
#
#     @allure.title('任务完成')
#     def test_finished(self):
#         '''任务完成'''
#         time.sleep(10)
#         s = self.bs.mysql.getstatus(self.bs.transportNo)
#         self.bs.log.debug('任务完成')
#         assert s[14][-1] == 'finished'
#
#
# if __name__ == '__main__':
#     pass
#
