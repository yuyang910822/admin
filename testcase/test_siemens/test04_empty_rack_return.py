# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/20 13:58
  @Auth : 于洋
  @File : tes04_empty_rack_return.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""

import unittest
from businessView.task_d import Empty_rack_return
class Empty_Rack(unittest.TestCase):
    '''返回空料架流程'''

    def test01(self):
        '''创建任务'''
        l = Empty_rack_return()
        self.assertTrue(l.create_task(), msg='fail')

    def test02(self):
        '''导航前往返回流程装载点'''
        l = Empty_rack_return()
        self.assertTrue(l.transit(), msg='fail')

    def test03(self):
        '''到达装载点'''
        l = Empty_rack_return()
        self.assertTrue(l.loading(), msg='fail')

    def test04(self):
        '''检测料架中'''
        l = Empty_rack_return()
        self.assertTrue(l.docking_in(), msg='fail')

    def test05_abnormal(self):
        '''检测料架异常'''
        l = Empty_rack_return()
        self.assertTrue(l.docking_erro(), msg='fail')

    def test06(self):
        '''人工处理'''
        l = Empty_rack_return()
        self.assertTrue(l.abnormal_one(), msg='fail')

    def test07(self):
        '''顶升完成'''
        l = Empty_rack_return()
        self.assertTrue(l.lift_asc_complete(), msg='fail')

    def test08(self):
        '''导航前往卸载点'''
        l = Empty_rack_return()
        self.assertTrue(l.go_unloading(), msg='fail')

    def test09(self):
        '''到达卸载点'''
        l = Empty_rack_return()
        self.assertTrue(l.arrive_unloading(), msg='fail')

    def test10(self):
        '''顶升下降完成'''
        l = Empty_rack_return()
        self.assertTrue(l.lift_desc_complete(), msg='fail')

    def test11(self):
        '''undokcing 中'''
        l = Empty_rack_return()
        self.assertTrue(l.undocking(), msg='fail')

    def test12(self):
        '''undokcing 完成'''
        l = Empty_rack_return()
        self.assertTrue(l.undocking_complete(), msg='fail')

    def test13(self):
        '''任务完成'''
        l = Empty_rack_return()
        self.assertTrue(l.finished(), msg='fail')

if __name__ == '__main__':
    unittest.main()