#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 22:24
# @Author  : Daisy
# @Site    :
# @File    : SimpleClassify.py
# @Software: PyCharm Community Edition
'''
简单分类:
使用词语进行筛选
兼有提取微博头
'''
import csv


def getWeiboHeader(startChar, endChar, yourStr):
    '''
    提取微博头
    :param startChar: 要提取的字符串开始符号,这里为 #
    :param endChar: 要提取的字符串结束符号,这里为 #
    :param yourStr: 要提取的字符串,这里为微博
    :return: 若有微博头则返回微博头,否则返回 -1
    '''
    start = yourStr.find(startChar)
    if start >= 0:
        start += len(startChar)
        end = yourStr.find(endChar, start)
        if end >= 0:
            return yourStr[start:end].strip()
        else:
            return -1


def writeData(dataList, headers, filename):
    '''
    将数据写成新的csv文件
    :param dataList: 要写入的List
    :param headers: 要写入的表头
    :param filename: 要写入的文件名
    :return: 无
    '''
    # print(dataList)
    with open(filename, 'a+', encoding='utf-8', newline='') as f:  # newline去行之间的空行
        w_csv = csv.DictWriter(f, headers)
        w_csv.writeheader()
        w_csv.writerows(dataList)
    f.close()


def classify():
    '''
    简单的使用 九寨 地震 两个关键词将数据进行切分
    :return: 返回 相关/不相关数据的数量
    '''
    posNum = 0
    negNum = 0
    num = 0
    dataName = 'sum.csv'
    posList = []
    negList = []
    sumList = []
    with open(dataName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            tempDict = {}
            if row['微博内容'].find('隧道') != -1 and row['微博内容'].find('事故') != -1:  # 入口
                # posTempDict = {}
                posNum += 1
                tempDict['微博内容'] = row['微博内容'].strip()
                tempDict['ID'] = posNum
                posList.append(tempDict)
            else:

                negNum += 1
                tempDict['微博内容'] = row['微博内容'].strip()
                tempDict['ID'] = negNum
                negList.append(tempDict)
            # num += 1
            # tempDict['ID'] = num
            sumList.append(tempDict)
    posHeaders = ['ID', '微博内容']
    negHeaders = ['ID', '微博内容']
    sumHeaders = ['ID', '微博内容']
    writeData(posList, posHeaders, '初步分类正相关.csv')
    writeData(negList, negHeaders, '初步分类负相关.csv')
    writeData(sumList, sumHeaders, '总表.csv')
    print('数据已分类完成')
    return posNum, negNum


if __name__ == '__main__':
    # test = getWeiboHeader('#',"#",'#你为何选择或不选择四川#【习近平向联合国世界旅游组织第22届全体大会致贺词】联合国世界旅游组织第22届全体大会13日在四川成都开幕。国家主席习近平向大会致贺词。习近平指出，旅游是不同国家、不同文化交流互鉴的重要渠道，是发展经济、增加就业的有效手段，也是提高人民生活水平的重要产业。 ????????...展开全文c')
    # print(test)
    posNum, negNum = classify()
    print('相关数量', posNum, '不相关数量', negNum)
