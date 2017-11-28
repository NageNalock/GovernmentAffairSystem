#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 23:46
# @Author  : Daisy
# @Site    : 
# @File    : ReadFile.py
# @Software: PyCharm Community Edition
'''
一个轮子
用来读简单分类好的数据的
1 为读取相关数据
0 为不相关数据
-1 为读取总表
已去停用词
已分词
'''


def readData(i):
    '''
    :param i: 1为相关数据 0为不相关数据
    :return: 词典字符串
    '''
    import csv
    import jieba
    stopWords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]

    returnList = []
    if i == 1:
        fileName = '初步分类正相关.csv'
        print('读取相关数据')
    elif i == 0:
        fileName = '初步分类负相关.csv'
        print('读取不相关数据')
    else:
        fileName = '总表.csv'
        print('读取总表')

    with open(fileName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            temp = str(row['微博内容'].split('\t')).replace(' ', '').replace('c', '')
            seg = jieba.cut(temp, cut_all=False)
            # temp = (list(set(seg) - set(stopWords) - set('\n')))
            returnList.append((list(set(seg) - set(stopWords) - set('\n'))))
            # returnList.append(list(seg))
    return returnList


if __name__ == '__main__':
    print(readData(3))
