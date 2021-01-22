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

import unittest
from businessView.task_a import Task_A


class  Feeding_A(unittest.TestCase):
    '''A点送料流程'''


    def test01(self):
        '''创建任务'''
        l = Task_A()
        self.assertTrue(l.create(), msg='fail')

    def test02(self):
        '''导航前往装载点'''
        l = Task_A()
        self.assertTrue(l.transit(), msg='fail')

    def test03(self):
        '''到达装载点'''
        l = Task_A()
        self.assertTrue(l.loading_one(), msg='fail')

    def test04(self):
        '''检测料架'''
        l = Task_A()
        self.assertTrue(l.docking_in_one(), msg='fail')

    def test05_abnormal(self):
        '''检测料架异常'''
        l = Task_A()
        self.assertTrue(l.docking_abnormal(), msg='fail')

    def test06(self):
        '''人工处理'''
        l = Task_A()
        self.assertTrue(l.abnormal_one(), msg='fail')

    def test07(self):
        '''顶升完成'''
        l = Task_A()
        self.assertTrue(l.lift_rise(), msg='fail')

    def test08(self):
        '''导航前往卸载点'''
        l = Task_A()
        self.assertTrue(l.go_unloading(), msg='fail')

    def test09(self):
        '''到达卸载点'''
        l = Task_A()
        self.assertTrue(l.arrive_unloading(), msg='fail')

    def test10(self):
        '''顶升下降完成'''
        l = Task_A()
        self.assertTrue(l.lift_decline(), msg='fail')

    def test11(self):
        '''undokcing'''
        l = Task_A()
        self.assertTrue(l.undocking(), msg='fail')

    def test12(self):
        '''是否带回空料架'''
        l = Task_A()
        self.assertTrue(l.choice_rack(), msg='fail')

    def test13(self):
        '''导航前往空料架点'''
        l = Task_A()
        self.assertTrue(l.empty_rack(), msg='fail')

    def test14(self):
        '''到达空料架点'''
        l = Task_A()
        self.assertTrue(l.arrive_empty_rack(), msg='fail')

    def test15(self):
        '''空料架装载点 docking中'''
        l = Task_A()
        self.assertTrue(l.empty_rack_docking(), msg='fail')

    def test16(self):
        '''空料架装载点 docking异常'''
        l = Task_A()
        self.assertTrue(l.empty_abnormal(), msg='fail')

    def test17(self):
        '''空料架点人工处理'''
        l = Task_A()
        self.assertTrue(l.abnormal_two(), msg='fail')

    def test18(self):
        '''顶升上升完成'''
        l = Task_A()
        self.assertTrue(l.empty_lift(), msg='fail')

    def test19(self):
        '''导航前往空料架卸载点'''
        l = Task_A()
        self.assertTrue(l.navigation_unloading(), msg='fail')

    def test20(self):
        '''到达空料架卸载点'''
        l = Task_A()
        self.assertTrue(l.arrive_empty_unloading(), msg='fail')

    def test21(self):
        '''顶升下降完成'''
        l = Task_A()
        self.assertTrue(l.lift(), msg='fail')

    def test22(self):
        '''空料架卸载点undocking完成'''
        l = Task_A()
        self.assertTrue(l.undocking_empry(), msg='fail')

    def test23(self):
        '''任务完成'''
        l = Task_A()
        self.assertTrue(l.finished(), msg='fail')




if __name__ == '__main__':
    r = Feeding_A()
    r.test01()


