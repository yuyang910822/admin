# # -*- coding: utf-8 -*-
# """
# @author: yuyang
# @time: 2020/12/30 20:56
# """
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
# class Create(unittest.TestCase):
#     """创建任务"""
#
#     testData = DoExcel(ExcelConfig.testDataPant, '创建任务')
#
#     @ddt.data(*testData.all())
#     def test_create(self,data):
#         """创建任务"""
#         new_expect = data['expect']
#         if "id" in data['request_json']:
#             data['request_json'] = data['request_json'].replace('id', new_id())
#         r = requests.request(method=data['type'],
#                              url=data['url'],
#                              headers=headers,
#                              json=json.loads(data['request_json']))
#         if 'BY' in data['expect']:
#             data['expect'] = data['expect'].replace('BY', r.json()['result']['transportNo'])
#             self.testData.result(data, 6, data['expect'])
#         try:
#             self.assertEqual(str(r.json()),data['expect'])
#         except AssertionError:
#             self.testData.result(data, 7, 'Fail')
#             self.testData.result(data, 8, '请求的Body：{}\n请求的参数：{}\n响应的json{}：'
#                                  .format(r.request.body, r.request.headers, r.json()))
#         else:
#             self.testData.result(data, 6, new_expect)
#             self.testData.result(data, 7, 'Pass')
#             self.testData.result(data, 8, '无')
#
#
# if __name__ == '__main__':
#     unittest.main()
#
