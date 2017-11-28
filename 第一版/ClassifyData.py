#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 17:54
# @Author  : Daisy
# @Site    : 
# @File    : ClassifyData.py
# @Software: PyCharm Community Edition

'''
分表并且为数据添加ID
五个表分别为 相关表 非相关表 无用信息表 错误表 总表(只包含相关与非相关)
每个相关或非相关信息都有一个唯一ID
相关数据与非相关数据也分别有一个自己ID
'''
import csv

dataID = 1  # 每条数据的唯一ID
posID = 1  # 相关评论的唯一ID
negID = -1  # 非相关评论的唯一ID
dcID = 1  # 辣鸡评论的唯一ID
errorID = 1  # 错误评论的唯一ID


def readOriginDataAddID(i):
    pos = []
    neg = []
    driedchicken = []
    error = []
    sum = []
    global dataID
    global posID
    global negID
    global dcID
    global errorID
    dataName = 'data/' + str(i) + '.csv'

    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            row['微博内容'] = (row['微博内容']).strip().rstrip(' ')
            row['dataID'] = dataID
            row['DataSource'] = i
            row['Score'] = 0
            dataID += 1
            if row['flag'] == '0':
                row['FeatureID'] = negID
                sum.append(row)
                neg.append(row)
                negID -= 1
            elif row['flag'] == '1':
                row['FeatureID'] = posID
                sum.append(row)
                pos.append(row)
                posID += 1
            elif row['flag'] == '-1':
                row['dcID'] = dcID
                dcID += 1
                driedchicken.append(row)
            else:
                row['errorID'] = errorID
                errorID += 1
                error.append(row)
    f.close()
    return pos, neg, driedchicken, error, sum


def writeData(dataList, headers, filename):
    fileName = '分表/' + filename + '.csv'
    # print(dataList)
    with open(fileName, 'a+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
        w_csv = csv.DictWriter(f, headers)
        w_csv.writeheader()
        w_csv.writerows(dataList)
    f.close()


if __name__ == '__main__':
    posFile = 'pos'
    negFile = 'neg'
    driedchickenFile = 'driedchicken'
    errorFile = 'error'
    sumFile = 'sum'

    posHeaders = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
                  'DataSource', 'Score']
    negHeaders = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
                  'DataSource', 'Score']
    dcHeaders = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'dcID', 'DataSource',
                 'Score']
    errorHeaders = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'errorID',
                    'DataSource', 'Score']
    sumHeaders = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
                  'DataSource', 'Score']
    for i in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        # for i in range(1, 16):
        posList, negList, dcList, errorList, sumList = readOriginDataAddID(i)
        print('读取第' + str(i) + '个文件')
        writeData(posList, posHeaders, posFile)
        print('写入pos')
        writeData(negList, negHeaders, negFile)
        print('写入neg')
        writeData(dcList, dcHeaders, driedchickenFile)
        print('写入dc')
        writeData(errorList, errorHeaders, errorFile)
        print('写入error')
        writeData(sumList, sumHeaders, sumFile)

        print('*****')
        # print(range(1, 2) , range(4, 16))
