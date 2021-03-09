# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/15 17:17 
  @Auth : 于洋
  @File : task_d.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import time
from common.basic_functions.seiemns_basic_functions import Task


class Empty_rack_return(Task):
    '''空料架返回流程'''


    def create_task(self):
        '''创建任务'''
        self.place_order('d')
        for i in range(1,101):
            time.sleep(1)
            if self.select_statuses() =='创建':
                return True
        return False

    def transit(self):
        '''导航前往返回流程装载点'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo,1) == 'processing':
                return True
        return False

    def loading(self):
        '''到达装载点'''
        self.finish()
        time.sleep(10)
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo,1) == 'finished':
                return True
        return False

    def docking_in(self):
        '''dokcing'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo,2) == 'processing':
                return True
        return False

    def docking_erro(self):
        '''docking异常'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo,2) == 'intervene':
                return True
        return False

    def abnormal_one(self):
        '''人工处理'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo,2) == 'intervene':
                self.resume()
                return True
        return False

    def lift_asc_complete(self):
        '''顶升完成'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 3) == 'finished':
                self.resume()
                return True
        return False

    def go_unloading(self):
        '''前往卸载点'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 4) == 'processing':
                self.resume()
                return True
        return False

    def arrive_unloading(self):
        '''到达卸载点'''
        time.sleep(5)
        self.finish()
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 4) == 'finished':
                self.resume()
                return True
        return False

    def lift_desc_complete(self):
        '''顶升下降完成'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 5) == 'finished':
                self.resume()
                return True
        return False

    def undocking(self):
        ''' undocking 中'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 6) == 'processing':
                self.resume()
                return True
        return False

    def undocking_complete(self):
        '''undocking 完成'''
        for i in range(1, 101):
            time.sleep(1)
            if self.getstatus(self.transportNo, 6) == 'finished':
                self.resume()
                return True
        return False

    def finished(self):
        '''任务完成'''
        time.sleep(30)
        if self.select_statuses() == '完成':
                return  True
        else:
            return False

