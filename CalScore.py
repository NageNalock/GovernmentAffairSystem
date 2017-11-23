#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/23 11:27
# @Author  : Daisy
# @Site    : 
# @File    : CalScore.py
# @Software: PyCharm Community Edition
import csv
import random
from NLPTest import myAip
import requests.packages.urllib3.exceptions
import requests.exceptions


def relevanceScore(str1, str2, model='BOW'):
    '''
    默认为"BOW",可选"BOW", "CNN", "GRNN"
    '''
    aip = myAip()
    result = aip.simnet(str1, str2, {'model': model})
    print('计算结果', result)

    try:
        return result['score']
    except KeyError or ConnectionError or TimeoutError or requests.packages.urllib3.exceptions.NewConnectionError or requests.exceptions.ConnectionError:
        return 0


def writeData(dataList):
    print("正在写入...")
    fileName = '分表/sum.csv'
    headers = ['\ufeff序号', '微博内容', '发布时间', '转发数', '评论数', '点赞数', '设备源', '微博ID', 'flag', 'dataID', 'FeatureID',
               'DataSource', 'Score']
    # print(dataList)
    with open(fileName, 'w+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
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


def readSumData():
    dataset = []
    dataName = '分表/sum.csv'
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            dataset.append(row)
    f.close()
    return dataset


def getDataScore(str_t):
    print('正在计算第条微博得分')
    sumDataList = readSumData()
    newData = []
    for sumData in sumDataList:
        print(sumData['dataID'])
        score_t = relevanceScore(str_t, sumData['微博内容'])
        print('原分分数', sumData['Score'])

        if score_t != 0:
            score = (score_t + float(sumData['Score'])) / 2
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
        dataDict[strNum] = getRandomData(i)  # 每个账号下随机选择10条
    # print(dataDict['1'][0]['微博内容'])  # 微博账号 该账号下的微博数据 具体的微博内容
    # getDataScore(dataDict['1'][0]['微博内容'])
    # dataList = []
    # for k in dataDict.keys():
    #     tempList = dataDict[k]
    #     for row in tempList:
    #         dataList.append(row)
    #
    # for data in dataList:
    #     str_te = data['微博内容']
    #     getDataScore(str_te, j)
    #     j += 1
    # result = relevanceScore('饶进阳没有女朋友', '饶进阳是个好人')
    # print(result)
    for k in ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']:
        for i in range(10):
            str_temp = dataDict[k][i]['微博内容']
            print('key:', k, 'i:', i)
            getDataScore(str_temp)
            print('已写入数据', k, ":", i)
