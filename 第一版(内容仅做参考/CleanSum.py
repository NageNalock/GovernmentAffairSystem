#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 12:48
# @Author  : Daisy
# @Site    : 
# @File    : CleanSum.py
# @Software: PyCharm Community Edition
'''
清理Sum表中的无效数据
'''
import csv


def readData():
    i = 0
    dataset = []
    dataName = '分表/sum.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            if row['Score'].isdigit() and (i < 2000):
                print('是数字')
                dataset.append(row)
                i += 1
    f.close()
    return dataset


def writeData(dataList):
    fileName = '分表/sum.csv'
    headers = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
               'DataSource', 'Score']
    # print(dataList)
    with open(fileName, 'w+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
        w_csv = csv.DictWriter(f, headers)
        w_csv.writeheader()
        w_csv.writerows(dataList)
    f.close()


writeData(readData())
