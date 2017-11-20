#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 12:29
# @Author  : Daisy
# @Site    : 
# @File    : TranTXT.py
# @Software: PyCharm Community Edition

import csv
import re


def readFile(i):
    fileName = 'data/' + str(i) + '.csv'
    with open(fileName, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row for row in reader]
    print('读入第' + str(i) + '个文件')
    pos = []
    neg = []
    driedchicken = []
    error = []
    for row in column:
        if row['flag'] == '0':
            neg.append(row['微博内容'])
        elif row['flag'] == '1':
            pos.append(row['微博内容'])
        elif row['flag'] == '-1':
            driedchicken.append(row['微博内容'])
        else:
            error.append(row['微博内容'])
    return pos, neg, driedchicken, error


def saveClassifyFile(filename, list):
    file = open(filename, 'a+', encoding='utf-8')
    newString = str(list).strip()
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # filterdata = re.findall(pattern, newString)
    # cleanedData = ''.join(filterdata)
    cleanedData = newString.replace('?', '').replace(']', '').replace(' ', '').replace('\'', '').replace('\\n', '').replace('[','')
    file.write(cleanedData)
    file.close()


if __name__ == '__main__':
    posFile = 'pos.txt'
    negFile = 'neg.txt'
    driedchickenFile = 'driedchicken.txt'
    errorFile = 'error.txt'
    # posF = open(posFile, 'w+', encoding='utf-8')
    # negF = open(negFile, 'w+', encoding='utf-8')
    # dcF = open(driedchickenFile, 'w+', encoding='utf-8')
    # errorF = open(errorFile, 'w+', encoding='utf-8')

    for i in range(1, 15):
        posList, negList, dcList, errorList = readFile(i)
        saveClassifyFile(posFile, posList)
        saveClassifyFile(negFile, negList)
        saveClassifyFile(driedchickenFile, dcList)
        saveClassifyFile(errorFile, errorList)
