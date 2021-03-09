# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/13 15:27 
  @Auth : 于洋
  @File : task_flow_A.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
from common.basic_functions.seiemns_basic_functions import Task


# @pytest.mark.usefixtures()
class Task_B(Task):
    '''任务B'''



    def create(self):
        '''创建任务'''
        self.place_order('b')
        if self.select_statuses() == '创建':
            return True
        else:
            return False

    def transit(self):
        '''导航前往装载点'''
        for i in range(1,101):
            time.sleep(5)
            self.logger.debug('当前模式：{}'.format(self.getstatus(self.transportNo, 1)))
            if self.getstatus(self.transportNo,1) == 'processing':
                self.logger.debug('导航中')
                return True
        return False

    def loading_one(self):
        '''到达装载点'''
        f = self.finish()
        self.logger.error(f)
        time.sleep(10)
        for i in range(1,101):
            time.sleep(1)
            self.logger.debug('当前模式：{}'.format(self.getstatus(self.transportNo, 1)))
            if self.getstatus(self.transportNo,1) == 'finished':
                self.logger.debug('到达装载点')
                return True
        return False

    def docking_in_one(self):
        '''检测料架'''
        for i in range(1,101):
            time.sleep(1)
            self.logger.debug('当前模式：{}'.format(self.getstatus(self.transportNo, 2)))
            if self.getstatus(self.transportNo,2) == 'processing':
                self.logger.debug('docking中')
                return True
        return False

    def docking_abnormal(self):
        '''检测料架异常'''
        for i in range(1, 101):
            time.sleep(1)
            f =self.getstatus(self.transportNo, 2)
            self.logger.debug('当前模式：{}'.format(f))
            if f  == 'intervene':
                self.logger.debug('docking中')
                return True
        return False

    def abnormal_one(self):
        '''人工处理'''
        l = self.resume()
        self.logger.error(l)
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 3)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def lift_rise(self):
        '''顶升完成'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 3)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def go_unloading(self):
        '''前往卸载点'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 4)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'processing':
                return True
        return False

    def arrive_unloading(self):
        '''到达卸载点'''
        self.finish()
        time.sleep(10)
        for i in range(1, 101):
            time.sleep(1)
            self.logger.debug('当前模式：{}'.format(self.getstatus(self.transportNo, 4)))
            if self.getstatus(self.transportNo, 4) == 'finished':
                return True
        return False

    def lift_decline(self):
        '''顶升完成'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 5)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def undocking(self):
        '''undocking'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 6)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 6)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'intervene':
                self.resume()
                time.sleep(10)
                return True
        return False

    def choice_rack(self):
        '''带回空料架'''
        for i in range(1,101):
            time.sleep(3)
            f = self.getstatus(self.transportNo,7)
            if f =='processing':
                time.sleep(10)
                f = self.rackYes()
            return True
        return False




    def empty_rack(self):
        '''导航前往空料架点'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 9)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'processing':
                return True
        return False

    def arrive_empty_rack(self):
        '''到达空料架点'''
        time.sleep(5)
        f = self.finish()
        self.logger.error(f)
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 9)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def empty_rack_docking(self):
        '''空料架docking中'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 10)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'processing':
                return True
        return False

    def empty_abnormal(self):
        '''空料料架docking异常'''
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 10)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'intervene':
                return True
        return False

    def abnormal_two(self):
        '''空料架异常转人工'''
        self.resume()
        time.sleep(10)
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 10)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def empty_lift(self):
        '''顶升完成'''
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 11)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def navigation_unloading(self):
        '''导航前往空料架卸载点'''
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 12)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'processing':
                return True
        return False

    def arrive_empty_unloading(self):
        '''到达空料架卸载点'''
        self.finish()
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 12)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def lift(self):
        '''顶升下载下降完成'''
        for i in range(1, 101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 13)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        return False

    def undocking_empry(self):
        '''undocking'''
        for i in range(1,101):
            time.sleep(1)
            f = self.getstatus(self.transportNo, 14)
            self.logger.debug('当前模式：{}'.format(f))
            if f == 'finished':
                return True
        for i in range(1,101):
            time.sleep(1)
            ff = self.getstatus(self.transportNo, 14)
            self.logger.debug('当前模式：{}'.format(ff))
            if ff == 'intervene':
                self.resume()
                time.sleep(10)
                return True
        return False

    def finished(self):
        '''任务完成'''
        time.sleep(10)
        if self.select_statuses() == '完成':
            return True
        else:
            return False

if __name__ == '__main__':
    r = Task_B()
    r.loading_one()

