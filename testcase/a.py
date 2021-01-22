# # -*- coding: utf-8 -*-
# """
# @author: yuyang
# @time: 2020/12/30 18:50
# """
#
#
# import unittest
# import json
# import requests
# import ddt
# from common.excel import DoExcel
# from config.path import ExcelConfig
#
#
# @ddt.ddt()
# class Login(unittest.TestCase):
#     """登录测试"""
#
#     testData = DoExcel(ExcelConfig.testDataPant, '登录')
#
#     @ddt.data(*testData.all())
#     def test_login(self,data):
#         r = requests.request(method=data['type'],
#                              url=data['url'],
#                              headers=ExcelConfig.headers,
#                              json=json.loads(data['request_json']))
#         if 'Token' in data['expect']:
#             data['expect']= data['expect'].replace('Token', r.json()['result']['token'])
#         try:
#             self.assertEqual(str(r.json()),data['expect'])
#         except AssertionError:
#             self.testData.result(data, 7, 'Fail')
#             self.testData.result(data, 8, '请求的Body：{}\n请求的参数：{}\n响应的json{}：'
#                                  .format(r.request.body, r.request.headers, r.json()))
#         else:
#             self.testData.result(data, 7, 'Pass')
#             self.testData.result(data, 8, '无')
#
# if __name__ == '__main__':
#     unittest.main()
#
