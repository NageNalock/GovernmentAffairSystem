#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 0:29
# @Author  : Daisy
# @Site    : 
# @File    : TF.py
# @Software: PyCharm Community Edition
'''
词频统计
'''
from ReadFile import readData
from nltk.probability import FreqDist, ConditionalFreqDist


def getTF(i=1):
    '''
    统计词频
    效果还不错
    :param i: 同ReadFile的i,默认为1
    :return: 已经排序过的词语dict
    '''
    wordsList = []
    word_f = FreqDist()
    for sentences in readData(i):
        for word in sentences:
            wordsList.append(word)
    # print(wordsList)
    for word in wordsList:
        word_f[word] += 1
    t = dict(word_f)
    sortedDict = sorted(t.items(), key=lambda e: e[1], reverse=True)
    return dict(sortedDict)


if __name__ == '__main__':
    print(getTF(1))
    print(getTF(2))
