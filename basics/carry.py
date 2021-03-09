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

    transportNo = ''



    def __init__(self,mysqlname,logname,logpath,testdatas):
        self.mysqlpath = read_yaml(mysql_dir)
        self.mysql = Mysql(self.mysqlpath[mysqlname])
        self.testdatas = read_yaml(testdatas)
        self.log = Mylog(name=logname,file=logpath)

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



    def create_task(self,task_type):
        '''下单'''
        data = self.testdatas['create_task']
        data['headers']['token'] = self.get_pda_token()
        data['json'][task_type]['originNo'] =time.strftime("%Y%m%d%H%M%S")
        self.log.info('pda下单参数:{}'.format(data))
        r = requests.request('post', url=data['url'], headers=data['headers'],json=data['json'][task_type ])
        self.log.info('返回值：{}'.format(r.json()))
        setattr(Carry_ability, 'transportNo', r.json()['result']['transportNo'])
        self.log.info('反射:{}'.format(self.transportNo))


    def select_task_status(self):
        '''查询任务状态'''
        data =self.testdatas['task_status']
        data['json']['transportNo'] = self.transportNo
        data['headers']['token'] = self.get_admin_token()
        self.log.info(data)
        try:
            r = requests.request('post',url=data['url'],headers=data['headers'],json=data['json'])
        except:
            raise
        self.log.info(r.json())
        self.log.info(r.json()['result']['items'][0]['statusDesc'])
        return r.json()['result']['items'][0]['statusDesc']


    def rack_task(self):
        """更新带回料架传参"""
        i = self.mysql.get_id(self.transportNo)
        self.log.debug(i)
        data = self.testdatas['rack']
        data['json']['detailList'][0]['taskDetailId'] = i[0]
        data['json']['taskId'] =i[1]
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
        data = self.testdatas['finish']
        try:
            r = requests.request('post', url=data)
        except:
            self.log.debug('finish 请求错误：{}'.format(r.json()))
            return False
        else:
            self.log.debug('请求成功')
            return True

    def resume(self):
        '''人工处理'''
        data= self.testdatas['resume']
        try:
            r = requests.request('post', url=data)
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

        for ll in range(1,100):
            # 任务状态集
            time.sleep(1)
            s = self.mysql.getstatus(self.transportNo)
            #判断状态集k与下标的值是否满足预期
            if s[k][i] == v:
                self.log.debug('满足状态条件:{}'.format(s[k][i]))
                return True
            self.log.info('当前状态不满足:{}'.format(s[k][i]))

        return False

