#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 17:11
# @Author  : Daisy
# @Site    :
# @File    : BalanceData.py
# @Software: PyCharm Community Edition
import csv
import random
from NLPTest import myAip


def relevanceScore(str1, str2, model='BOW'):
    '''
    默认为"BOW",可选"BOW", "CNN", "GRNN"
    '''
    aip = myAip()
    result = aip.simnet(str1, str2, {'model': model})
    return result


def writeData(dataList):
    fileName = 'score.csv'
    headers = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
               'DataSource', 'Score']
    # print(dataList)
    with open(fileName, 'a+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
        w_csv = csv.DictWriter(f, headers)
        w_csv.writeheader()
        w_csv.writerows(dataList)
    f.close()


def readData(i):
    dataset = []
    dataName = '分表/pos.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            if row['DataSource'] == str(i):
                dataset.append(row)
    f.close()
    return dataset


def readSumdata(i):
    dataset = []
    dataName = 'score.csv'
    if i == 1:
        dataName = '分表/sum.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            dataset.append(row)
    f.close()
    return dataset


def getDataScore(str_t, num):
    print('正在计算第' + str(num) + '条微博得分')
    sumDataList = readSumdata(num)
    newData = []
    for sumData in sumDataList:
        print(sumData['微博内容'])
        if num == 1:
            score = relevanceScore(str_t, sumData['微博内容'])
        else:
            score_t = relevanceScore(str_t, sumData['微博内容'])
            score = (score_t + int(sumData['Score'])) / 2
        sumData['Score'] = score
        newData.append(sumData)
    writeData(newData)


def getRandomData(i):
    dataset = []
    returnData = []
    dataName = '分表/pos.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            if row['DataSource'] == str(i):
                dataset.append(row)
    length = len(dataset)
    for i in range(10):
        randomNum = random.randint(0, length - 1)
        returnData.append(dataset[randomNum])
    f.close()
    return returnData


if __name__ == '__main__':
    dataDict = {}
    j = 1
    for i in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        strNum = str(i)
        dataDict[strNum] = getRandomData(i)
    dataList = []
    for k in dataDict.keys():
        tempList = dataDict[k]
        for row in tempList:
            dataList.append(row)

    for data in dataList:
        str_te = data['微博内容']
        getDataScore(str_te, j)
        j += 1
        # print(dataDict)
        # for k in dataDict.keys():
        #     print('***')
        #     print(len(dataDict[k]))
