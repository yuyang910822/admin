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
import requests,yaml,time,json,os
from log.get_log import log
from common.mysql import Mysql
from config.path import *
class Task(Mysql):



    yy = open(yaml_path,encoding='utf-8')
    d = yaml.load(yy, Loader=yaml.FullLoader)
    log = log()
    transportNo = ''

    def pda_headers(self):
        '''更新pda端headers'''
        headers = self.d['pda']['headers']
        r = requests.request('post',url=self.d['pda']['url'],headers=headers,json=json.loads(self.d['pda']['data']))
        headers['token'] =  r.json()['result']['token']
        return headers

    def ye_headers(self):
        '''更新业务平台headers'''
        headers = self.d['admin']['headers']
        r = requests.request('post',url=self.d['admin']['url'],headers=headers,json=json.loads(self.d['admin']['data']))
        headers['token'] =  r.json()['result']['token']
        return headers

    def amr_headers(self):
        return self.d['fta']

    def order_parameters(self,p):
        '''生成下单参数'''
        data = str(self.d['data']['create'][p])
        data = data.replace('id', time.strftime("%Y%m%d%H%M%S"))
        self.log.debug('pda下单参数:{}'.format(data))
        return data

    def select_parameters(self):
        '''更新查询参数'''
        data = str(self.d['data']['page'])
        data = data.replace('BY', self.transportNo)
        self.log.debug('查询任务状态入参：{}'.format(data[45:-2]))
        return data

    def place_order(self,p):
        '''下单'''
        r = requests.request('post', url=self.d['url']['create'], headers=self.pda_headers(), json=json.loads(self.order_parameters(p)))
        self.log.debug('返回值：{}'.format(r.json()))
        setattr(Task, 'transportNo', r.json()['result']['transportNo'])
        self.log.debug('反射:{}'.format(self.transportNo))

    def select_statuses(self):
        '''查询任务状态'''
        r = requests.request('post',url=self.d['url']['page'],headers=self.ye_headers(),json=json.loads(self.select_parameters()))
        self.log.debug('查询任务状态结果:{}'.format(r.json()['result']['items'][0]['statusDesc']))
        return r.json()['result']['items'][0]['statusDesc']

    def rack_task(self):
        """更新带回料架传参"""
        i = Mysql().get_id(self.transportNo)
        self.log.debug(i)
        data = str(self.d['data']['rack'])
        data1 = data.replace('888',str(i[0]))
        data2 = data1.replace('AAA',str(i[1]))
        self.log.debug('{}'.format(data2))
        return data2

    def rackYes(self):
        '''带回料架请求'''
        r = requests.request('post',url=self.d['url']['rack'],headers= self.amr_headers(),json=json.loads(self.rack_task()))
        self.log.debug(r.text)
        return r.json()

    def finish(self):
        '''提前到达'''
        r = requests.request('post', url=self.d['url']['finish'])
        self.log.debug('提前到达结果{}'.format(r.text))
        return r.json()

    def resume(self):
        '''人工处理'''
        r = requests.request('post', url=self.d['url']['resume'])
        self.log.debug(r.text)
        return r.json()


if __name__ == '__main__':
    a = Task()
    print(a.ye_headers())