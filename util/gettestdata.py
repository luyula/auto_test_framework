""" 
@author: lileilei
@file: ddd.py 
@time: 2018/1/19 11:43 
"""
import xlrd
from util import log
from  config import root_path

logs = log.log_message('获取数据')


def huoqu_test(filepath, index):
    '''
    参考：https://www.2cto.com/kf/201805/745595.html
    :param filepath:  测试数据存放路径
    :param index:   Execl 里面sheet(工作表)的下标 从0开始
    :return:
    '''
    try:
        file = xlrd.open_workbook(filepath)
        sheet = file.sheets()[index - 1]  # index 表单 默认一个Excel表中只存储一个表单  从0开始
        nrows = sheet.nrows  # 获取表单行数
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['id'] = sheet.cell(i, 0).value  # 获取单元格内容
            dict_canshu.update(eval(sheet.cell(i, 2).value))
            dict_canshu.update(eval(sheet.cell(i, 3).value))
            listdata.append(dict_canshu)
        logs.logger.info('获取%s内第%s个sheet(工作表)的测试数据' % (filepath, index))
        logs.logger.info('测试数据listdata：%s'%listdata)
        return listdata
    except Exception as e:
        logs.logger.error('获取测试用例数据失败，原因：%s' % e)


if __name__ == '__main__':
    file_path=root_path + '\\data\\case.xlsx'
    huoqu_test(file_path, 1)
