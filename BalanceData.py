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


def readData(i):
    dataset = []
    dataName = '分表/pos.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            if row['DataSource'] == str(i):
                dataset.append(row)
    return dataset


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
    return returnData


def relevanceScore(str1, str2, model='BOW'):
    '''
    默认为"BOW",可选"BOW", "CNN", "GRNN"
    '''
    aip = myAip()
    result = aip.simnet(str1, str2, {'model': model})
    return result


if __name__ == '__main__':
    dataDict = {}
    j = 0
    for i in [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        strNum = str(i)
        dataDict[strNum] = getRandomData(i)
        # print(dataDict)
        # for k in dataDict.keys():
        #     print('***')
        #     print(len(dataDict[k]))
