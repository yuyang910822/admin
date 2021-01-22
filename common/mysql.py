import pymysql,time
from common.settings import configData
from log.get_log import log

data = configData()['mysql']


class Mysql():
    '''数据库操作'''
    def __init__(self,databaseName='test_siemens_rpm'):
        self.db = pymysql.connect(host= data['host'],
                                 user = data['user'],
                                 password = data['password'],
                                 port = data['port'],
                                 charset = data['charset'],
                                 database= databaseName)
        self.c = self.db.cursor()


    def select(self,sql,fetch=True):
        '''输入sql查询数据'''
        try:
            self.c.execute(sql)
        except:
            self.db.rollback()
        else:
            if fetch == True:
                return self.c.fetchone()[0]
            else:
                return self.c.fetchall()[0]
        finally:
            self.db.close()
            self.c.close()

    def delect(self):
        print()


    def getstatus(self,by,n):
        '''通过status和index查询当然动作的状态'''
        try:
           t =  self.c.execute("SELECT rt.index,rt.type,rt.status FROM t_transport tt INNER JOIN t_robot_task trt ON trt.`business_id` = "
                               "tt.`id` INNER JOIN t_rcs_job trj ON trj.`robot_task_id` = trt.`id` INNER JOIN t_rcs_task"
                               " rt ON rt.`job_id` = trj.`id` WHERE tt.`transport_no` = '{}'".format(by))
        except:
            self.db.rollback()
        else:
            status = {}
            for i in list(self.c.fetchall()):
                status[i[0]] = i[1:]
            return list(status[n])[-1]


    def get_id(self,by):
        '''获取id替换是否带回了解的入参'''
        try:
            self.c.execute('SELECT trtd.id,trtd.task_id FROM t_robot_task_detail trtd INNER JOIN t_robot_task trt ON trt.id = trtd.task_id INNER JOIN t_transport tt ON tt.id = trt.business_id WHERE tt.transport_no = "{}"'.format(by))
            s = self.c.fetchall()[1]
            return list(s)
        except:
            self.db.rollback()



if __name__ == '__main__':
    a =Mysql()
    # print(a.get_status('BY20210113002879','pending'))

