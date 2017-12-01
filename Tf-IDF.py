#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 23:59
# @Author  : Daisy
# @Site    : 
# @File    : Tf-IDF.py
# @Software: PyCharm Community Edition
'''
TF-IDF进行关键词提取
'''

'''
如果某个词或短语在一篇文章中出现的频率TF高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类。
即 TF * IDF
https://www.cnblogs.com/chenbjin/p/3851165.html

这里正常统计词频
而逆向文件频率的文件数则改为评论数
算法退化?
'''
from TF import getTF, readData
from SimpleClassify import writeData
# 直接使用

def saveDictAsTxt(filename, dataDict):
    '''
    将词典保存为txt文件
    :param filename: 保存的文件名
    :param dataDict: 保存的词典
    :return: 无
    '''
    retrunStr = ''
    for key in dataDict:
        tempStr = str(key) + ':' + str(dataDict[key]) + '\n'
        retrunStr += tempStr
    f = open(filename, 'w+', encoding='utf-8')
    f.write(retrunStr)
    print('已保存', filename)
    f.close()


def normalization(wordDict):
    '''
    归一化
    :param wordDict: 输入的词典
    :return: 返回出的词典
    '''
    minF = 1
    maxF = 1
    for word in wordDict:
        minF = min(minF, wordDict[word])
        maxF = max(maxF, wordDict[word])
    # print(minF)
    # print(maxF)
    # print('数据归一化前', wordDict.items())
    for word in wordDict:
        temp = wordDict[word]
        wordDict[word] = (temp - minF) / (maxF - minF)
    # print('数据归一化后', wordDict.items())
    return wordDict


def imTFandIDF():
    '''
    特征TF减去总的TF
    :return: 词典类型的结果
    '''
    posDict = normalization(getTF(1))
    sumDict = normalization(getTF(2))

    returnDict = {}
    for key in posDict:
        try:
            temp = posDict[key] - sumDict[key]
            returnDict[key] = temp

        except KeyError:
            continue
    saveDictAsTxt('pos.txt', posDict)
    saveDictAsTxt('sum.txt', sumDict)
    saveDictAsTxt('rt.txt', returnDict)

    return dict(returnDict)


if __name__ == '__main__':
    finalDict = imTFandIDF()
    fianl = sorted(finalDict.items(), key=lambda e: e[1], reverse=True)
    print(fianl)
    saveDictAsTxt('最后结果.txt', dict(fianl))
'''
改良思考
我们是否可以将相关评论作为TF的统计
将相关+不相关作为IDF的统计
但是这样的话相关系数就会发生变化,需要另外寻找相关系数

这里将TF 与 IDF 归一化
同时将原来的TF*IDF的方式改为TF-IDF的方式
排除掉了多个高频项的影响
'''
