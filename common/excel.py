import openpyxl,re
# from config.path import ExcelConfig
import random,time
class DoExcel():

    def __init__(self,file_name,sheet_name):
        self.f = file_name
        self.s = sheet_name
        self.workbook = openpyxl.load_workbook(self.f)
        self.sheet = self.workbook[self.s]


    # def open(self):
    #     """打开工作薄，选择表单"""
    #     self.workbook = openpyxl.load_workbook(self.f)
    #     self.sheet = self.workbook[self.s]
    #     return self.sheet

    def close(self):
        """关闭工作薄对象，释放内存"""
        self.workbook.close()


    def firstline(self) -> list:
        """首行信息"""
        return [i.value for i in self.sheet[1]]

    def all(self) -> list:
        """测试数据"""
        # self.sheet
        testdata = []
        maxrow = self.sheet.max_row
        if  maxrow <= 1:
            print("无法拼接数据，请检查{}的{}表".format(self.f,self.s))
        elif maxrow == 2:
            ii = []
            for i in self.sheet[2:maxrow]:
                ii.append(i.value)
            z = dict(zip(self.firstline(), ii))
            testdata.append(z)
        else:
            ii = []
            for i in self.sheet[1:maxrow]:
                # ii = []
                for j in i:
                    ii.append(j.value)
                # z = dict(zip(self.firstline(), ii))
                # testdata.append(z)
        self.close()
        return ii






    def result(self,data,new,v):

        # 写入数据
        self.sheet.cell(data+1,new,v)
        # 保存文件
        self.workbook.save(r"C:\Users\yuyang\Downloads\kk仓.xlsx")
        # 关闭工作薄
        self.close()



    def updataData(self,data):
        """提取json进行更新"""
        name=str(random.randint(100, 9999999))
        code=str(random.randint(100, 9999999))
        data1=str(random.randint(100, 9999999))
        if name !=code:
            if re.search("name",str(data)):
                data["json"] = data["json"].replace("name",name)
            if re.search("code",str(data)):
                data["json"] = data["json"].replace("code",code)
            if re.search("data",str(data)):
                data["json"] = data["json"].replace("data",data1)



if __name__ == "__main__":
    import json
    a = DoExcel(r"C:\Users\yuyang\Downloads\kk仓.xlsx","Sheet1")
    # a.result(1,1,'OT1029821050700000066')
    a.result(109,4,'3CJ441')