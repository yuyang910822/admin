# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/1/14 13:39
  @Auth : 于洋
  @File : task.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
-------------------------------------------------
"""
import requests,time
from common.mysql import Mysql
from common.log import Mylog
from common.return_yaml import *


class Carry_ability():
    '''基础功能封装'''


    # transportNo = ''



    def __init__(self,mysqlname,logname,logpath,testdatas):
        # self.mysqlpath = read_yaml(mysql_dir)
        # self.mysql = Mysql(mysqlpath[mysqlname])

        self.mysql = Mysql(read_yaml(mysql_dir)[mysqlname])
        self.testdatas = read_yaml(testdatas)
        self.log = Mylog(name=logname,file=logpath)

    finish = 'http://10.3.1.98:7000/api/jobs/finish'
    resume = 'http://10.3.1.98:7000/api/jobs/resume_sub_task'

    def get_pda_token(self):
        '''获取pda端token'''
        data = self.testdatas['pda_login']
        r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
        return r.json()['result']['token']


    def get_admin_token(self):
        '''获取业务平台端token'''
        data = self.testdatas['admin_login']
        r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
        return  r.json()['result']['token']



    def create_task(self,taskname):
        '''下单'''
        data = self.testdatas[taskname]
        data['headers']['token'] = self.get_pda_token()
        data['json']['originNo'] =time.strftime("%Y%m%d%H%M%S")
        self.log.debug('pda下单参数:{}'.format(data))
        r = requests.request('post', url=data['url'], headers=data['headers'],json=data['json'])
        self.log.debug('返回值：{}'.format(r.json()))
        setattr(Carry_ability, 'transportNo', r.json()['result']['transportNo'])
        self.log.debug('反射:{}'.format(self.transportNo))


    def select_task_status(self):
        '''查询任务状态'''
        data =self.testdatas['task_status']
        data['json']['transportNo'] = self.transportNo
        data['headers']['token'] = self.get_admin_token()
        self.log.debug(data)
        try:
            r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
        except:
            raise
        self.log.debug(r.json()['result']['items'][0]['statusDesc'])
        return r.json()['result']['items'][0]['statusDesc']


    def rack_task(self):
        """更新带回料架传参"""
        i = self.mysql.get_id(self.transportNo)
        self.log.debug(i)
        data = self.testdatas['rack']
        data['json']['detailList'][0]['taskDetailId']= i[0]
        data['json']['taskId'] = i[1]
        self.log.debug('请求参数:{}'.format(data))
        for i in range(1,10):
            time.sleep(1)
            s = self.mysql.getstatus(self.transportNo)
            if s[7][-1] == 'processing':
                try:
                    r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
                    self.log.debug('返回参数：{}'.format(r.json()))
                except:
                    self.log.error('带回料架请求错误')
                    return False
                else:
                    return True


    def finish(self):
        '''提前到达'''

        try:
            r = requests.request('post', url=self.finish)
        except:
            self.log.error('finish 请求错误：{}'.format(r.json()))
            return False
        else:
            self.log.debug('请求成功')
            return True

    def resume(self):
        '''人工处理'''

        try:
            r = requests.request('post', url=self.resume)
            self.log.debug('resume 请求{}'.format(r.json()))
        except:
            return False
        else:
            if r.json()['result']['data'] == 'resume sub task success':
                return True
            else:
                return False



    def task_status(self,k,v,i=-1):
        '''获取任务集指定k的v'''
        for ll in range(1,1000):
            # 任务状态集
            time.sleep(2)
            s = self.mysql.getstatus(self.transportNo)
            #判断状态集k与下标的值是否满足预期
            if s[k][i] == v:
                self.log.debug('满足状态条件:{}'.format(s[k][i]))
                return True
        self.log.debug('当前状态不满足:{}'.format(s[k][i]))

        return False



    def docking(self,k,i=-1):
        for ll in range(1,100):
            time.sleep(1)
            s = self.mysql.getstatus(self.transportNo)
            self.log.debug('undocking:{}'.format(s))
            if s[k][i] == 'finished' or s[k][i] == 'intervene':
                self.log.debug('docking状态{}'.format(s[k][i]))
                if s[k][i] == 'finished':
                    return True
                elif s[k][i] == 'intervene':
                    self.resume()
                    return True
                elif s[k][i] == 'processing':
                    time.sleep(3)
                    self.finish()
        return False


    def loadingFinish(self):
        '''出发'''
        time.sleep(3)
        data = self.testdatas['loadingFinish']
        data['json']['detailList'][0]['taskDetailId'] = self.mysql.get_id_task_id(self.transportNo)[0][0]
        data['json']['taskId'] = self.mysql.get_id_task_id(self.transportNo)[0][1]
        self.log.debug(data)
        try:
            r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
            self.log.debug('1:{}'.format(r.request.body))
            self.log.debug('出发结果：{}'.format(r.json()))
        except:
            return False
        else:
            return True


    def receiveMaterials(self):
        '''物料接收'''
        time.sleep(3)
        data = self.testdatas['loadingFinish']
        data['json']['detailList'][0]['taskDetailId'] = self.mysql.get_id_task_id(self.transportNo)[1][0]
        data['json']['taskId'] = self.mysql.get_id_task_id(self.transportNo)[1][1]
        try:
            r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
            self.log.debug('出发结果：{}'.format(r.json()))
        except:
            return False
        else:
            return True

    def division(self):
        '''作业分工'''
        data = self.testdatas['division']
        data['headers']['token'] = self.get_pda_token()
        self.log.debug(data)
        r = requests.request('put',url=data['url'],headers=data['headers'],json=data['json'])
        self.log.debug('作业分工结果{}'.format(r.json()))

if __name__ == '__main__':
    print(logs_dir)
    print(os.path.join(logs_dir,'siemens.log'))
    print(blue_yaml)
    bs = Carry_ability(mysqlname='standard_mysql', logname='blue', logpath=os.path.join(logs_dir,'siemens.log'), testdatas=blue_yaml)
    bs.division()

