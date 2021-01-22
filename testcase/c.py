# # -*- coding: utf-8 -*-
# """
# @author: yuyang
# @time: 2020/12/31 0:21
# """
#
#
# import unittest
# import json
# import requests
# import ddt
# from common.excel import DoExcel
# from config.path import ExcelConfig
# from common.settings import *
#
# #
# @ddt.ddt()
# class Logout(unittest.TestCase):
#     """登出"""
#
#     testData = DoExcel(ExcelConfig.testDataPant, '登出')
#
#
#
#     @ddt.data(*testData.all())
#     def test_logout(self,data):
#         """退出测试集"""
#         r = requests.request(method=data['type'],
#                              url=data['url'],
#                              headers=headers,
#                              json=json.loads(data['request_json']))
#         try:
#             self.assertEqual(str(r.text),data['expect'])
#         except AssertionError:
#             self.testData.result(data, 8, 'Fail')
#             self.testData.result(data, 9, '请求的Body：{}\n请求的参数：{}\n响应的json{}：'
#                                  .format(r.request.body, r.request.headers, r.json()))
#         else:
#             self.testData.result(data, 8, 'Pass')
#             self.testData.result(data, 9, '无')
#
#
#
# if __name__ == '__main__':
#     unittest.main()
