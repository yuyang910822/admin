import pymysql


from common.return_yaml import *

class Mysql():
    '''数据库操作'''

    def __init__(self,data):
        self.db = pymysql.connect(host= data['host'],user = data['user'],password = data['password'],
                                  port = data['port'],charset = data['charset'],database= data['database'])
        # ,cursorclass=pymysql.cursors.DictCursor
        self.c = self.db.cursor()


    def closes(self):
        '''
        关闭游标
        '''
        self.db.close()
        self.c.close()


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



    def delect(self):
        print()


    def getstatus(self,by):
        """
        获取任务状态
        """
        try:
            t = self.c.execute("SELECT `index`,type,status FROM t_rcs_task WHERE "
                               "job_id=(SELECT id FROM t_rcs_job WHERE "
                               "NAME =(SELECT task_no FROM t_robot_task WHERE "
                               "business_id =(SELECT id FROM t_transport WHERE transport_no = '{}')))".format(by))
                # "SELECT rt.index,rt.type,rt.status FROM t_transport tt INNER JOIN t_robot_task trt ON trt.`business_id` = "
                # "tt.`id` INNER JOIN t_rcs_job trj ON trj.`robot_task_id` = trt.`id` INNER JOIN t_rcs_task"
                # " rt ON rt.`job_id` = trj.`id` WHERE tt.`transport_no` = '{}'".format(by))
        except :
            self.db.rollback()
            raise
        else:

            status = {}
            for i in list(self.c.fetchall()):
                status[i[0]] = i[1:]
            self.db.commit()
            return status




    def get_id(self,by):
        '''获取id替换是否带回了解的入参'''
        print(by)
        try:
            self.c.execute('SELECT trtd.id,trtd.task_id FROM t_robot_task_detail trtd INNER JOIN t_robot_task trt ON'
                           ' trt.id = trtd.task_id INNER JOIN t_transport tt ON tt.id = trt.business_id'
                           ' WHERE tt.transport_no = "{}"'.format(by))
            s = self.c.fetchall()[1]
        except:
            self.db.rollback()
        else:
            return list(s)

    def get_id_task_id(self,by):
        try:
            self.c.execute("SELECT id,task_id FROM t_robot_task_detail WHERE task_id = (SELECT id FROM t_robot_task WHERE business_id =(SELECT id FROM t_transport WHERE transport_no = '{}'))".format(by))
        except:
            self.db.rollback()
        else:
            return self.c.fetchall()



    def getrobotcoude(self):
        try:
            self.c.execute('SELECT distinct t1.robot_code,t2.internal_station_name FROM t_robot_task t1, t_robot_task_detail t2 WHERE t1.id = t2.`task_id`  AND t1.`biz_type` = "PICK_LOCATION"   AND t1.`status` = 200   AND t2.`status` = 100 and t2.arrival_time is not null')
        except:
            self.db.rollback()
        else:
            self.db.commit()
            return self.c.fetchall()

if __name__ == '__main__':
    mysqlpath = read_yaml(mysql_dir)

    a =Mysql(data=mysqlpath['jj'])

    b = a.getrobotcoude()
    print(b[0]) #('001', '3CE011')

