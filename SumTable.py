#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 14:55
# @Author  : Daisy
# @Site    : 
# @File    : SumTable.py
# @Software: PyCharm Community Edition
'''
把数据汇集到一个表上
'''

import csv


def readData(i):
    print('正在读取', i, '号文件')
    sumData = []
    tableName = 'data/'  + str(i)  + '.csv'
    with open(tableName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            row['微博内容'] = (row['微博内容']).strip().rstrip(' ')
            sumData.append(row)
    f.close()
    return sumData


def writeData(dataList, headers, filename):
    fileName = filename + '.csv'
    # print(dataList)
    with open(fileName, 'a+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
        w_csv = csv.DictWriter(f, headers)
        w_csv.writeheader()
        w_csv.writerows(dataList)
    f.close()


if __name__ == '__main__':
    sumHeaders = ['\ufeff序号', '微博内容', '是否原创','转发内容','发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID']
    fileName = 'sum'
    for i in range(1, 73):  # 入口
        print('正在写入', i, '号文件')
        sumList = readData(i)
        writeData(sumList, sumHeaders, fileName)
