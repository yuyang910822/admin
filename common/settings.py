# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/8/2 22:58
"""
import os,time,random,yaml
"""
时间
路径
接口

"""
import requests,json

def gettime():
    '''日期时间'''
    return time.strftime("%Y-%m-%d %H:%M:%S")


def configData():
    y =open(config_config,encoding='utf-8')
    data =yaml.load(y,Loader=yaml.FullLoader)
    y.close()
    return data



homePath= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_config = os.path.join(homePath,'config\configFail.yaml')


def new_id():
    time.sleep(1)
    return time.strftime("%Y%m%d%H%M%S")

pda_headers = {
  'workSpaceId':'2001',
  'workSpaceCode':'01',
  'Content-Type':'application/json;charset=UTF-8',
  'userId':'2001',
  'token':'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTA1MzYxNzMsImp0aSI6InB2dTIwNjh5WDMwWFlqamlRTUpnVWciLCJpYXQiOjE2MTA1MTgxNzMsInVzZXIiOiJ7XCJpZFwiOjIwMDEsXCJ1c2VyTmFtZVwiOlwieG16X2FkbWluXCIsXCJyZWFsTmFtZVwiOlwieG16X2FkbWluXCIsXCJjdXN0b21lcklkXCI6NzksXCJjdXN0b21lckNvZGVcIjpcIjEwMTVcIixcInVzZXJFeHRJbmZvQm9MaXN0XCI6W3tcImlkXCI6MjAwMSxcInVzZXJJZFwiOjIwMDEsXCJjdXN0b21lcklkXCI6NzksXCJjdXN0b21lckNvZGVcIjpcIjEwMTVcIixcImN1c3RvbWVyTmFtZVwiOlwi6KW_6Zeo5a2QXCIsXCJ3b3JrU3BhY2VJZFwiOjIwMDEsXCJ3b3JrU3BhY2VOYW1lXCI6XCLopb_pl6jlrZAwMDFcIixcIndvcmtTcGFjZUNvZGVcIjpcIjAxXCJ9XSxcInJvbGVJZFwiOjIsXCJyb2xlTmFtZVwiOlwi5a6i5oi3566h55CG5ZGYXCIsXCJpc0luaXRQYXNzd29yZFwiOjEsXCJkZXZpY2VUeXBlXCI6M30ifQ.27cx4M3_h19ZKTfxVZVp964pLJGB7efGQRx67tdpEZA',
  'customerId':'79',
  'deviceType':'3'
}


def get_ye_headers():
    headers = {
        'Content-Length':'70',
        'userId':'undefined',
        'Content-Type':'application/json;charset=UTF-8',
        'deviceType':'1',
    }
    r =requests.request('post',url='http://gateway.siemens.test.internal.forwardx.com/base-server/auth/login',
                        headers=headers,
                        json= {"userName":"xmz_admin","password":"64f19f650121e3b5a839694c237bd2f1"})
    ye_headers = {
      'Content-Length':'63',
      'deviceType':'1',
      'workSpaceCode':'01',
      'Content-Type':'application/json;charset=UTF-8',
      'userId':'2001',
      'token':'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTA1NTMxMjcsImp0aSI6IkhlSF9JX3I3NmZTLWtUMkwycmRVV1EiLCJpYXQiOjE2MTA1MzUxMjcsInVzZXIiOiJ7XCJpZFwiOjIwMDEsXCJ1c2VyTmFtZVwiOlwieG16X2FkbWluXCIsXCJyZWFsTmFtZVwiOlwieG16X2FkbWluXCIsXCJjdXN0b21lcklkXCI6NzksXCJjdXN0b21lckNvZGVcIjpcIjEwMTVcIixcInVzZXJFeHRJbmZvQm9MaXN0XCI6W3tcImlkXCI6MjAwMSxcInVzZXJJZFwiOjIwMDEsXCJjdXN0b21lcklkXCI6NzksXCJjdXN0b21lckNvZGVcIjpcIjEwMTVcIixcImN1c3RvbWVyTmFtZVwiOlwi6KW_6Zeo5a2QXCIsXCJ3b3JrU3BhY2VJZFwiOjIwMDEsXCJ3b3JrU3BhY2VOYW1lXCI6XCLopb_pl6jlrZAwMDFcIixcIndvcmtTcGFjZUNvZGVcIjpcIjAxXCJ9XSxcInJvbGVJZFwiOjIsXCJyb2xlTmFtZVwiOlwi5a6i5oi3566h55CG5ZGYXCIsXCJpc0luaXRQYXNzd29yZFwiOjEsXCJkZXZpY2VUeXBlXCI6MX0ifQ.bq20BG2QSpl5Rwa_bCFbWcpXD-nWtAADK1cETyVqUBM',
      'customerId':'79',
      'workSpaceId':'2001',

    }
    ye_headers['token'] = r.json()['result']['token']
    return ye_headers

if __name__ == '__main__':
    print(get_ye_headers())
