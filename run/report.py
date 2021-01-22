# -*- coding: utf-8 -*-
"""
@author: yuyang
@time: 2020/7/31 14:09
"""
import unittest,sys,os,time,smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from HTMLTestRunner import HTMLTestRunner





def run():
    # 生成测试报告HTML文件。

    # print(a)
    dir = '../testcase'
    report_dir = '../reports'
    now = time.strftime("%Y%m%d%H%M%S")
    b = unittest.defaultTestLoader.discover(dir, pattern='test001*.py')
    report_name = report_dir + '/' + now + 'Result.html'
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,title='【西门子-PDA】--接口自动化报告，测试结果如下：',
                                                description="运行环境 :PDA")
        # 执行测试用例文件
        runner.run(b)



def start_mail():
     #定义正文
     file = '../reports'
     lists = os.listdir(file)
     lists.sort(key=lambda fn: os.path.getatime(file + '/' + fn))
     file_path = os.path.join(file, lists[-1])
     fy = open(file_path, mode='rb')
     m =fy.read()
     fy.close()

     #邮件发送
     sender = 'smtp.163.com'
     receivers = ['yuyang@forwardx.com']
     message = MIMEMultipart('mixed')
     message1 = MIMEText(m,'html','utf-8')
     message.attach(message1)
     message['From'] = "于洋"
     message['To'] = ";".join(receivers)
     subject = '西门子'+ time.strftime('%Y-%m-%d')+'【西门子-PDA】--接口自动化'
     message['Subject'] = subject
     smtpObj = smtplib.SMTP()
     smtpObj.connect(sender,25)
     smtpObj.login('yangyu110221@163.com','yy123123')
     smtpObj.sendmail('yangyu110221@163.com',receivers, message.as_string())
     smtpObj.quit()
     print("发送成功")



if __name__ == '__main__':
    sys.path.append('../')
    run()
    # start_mail()

