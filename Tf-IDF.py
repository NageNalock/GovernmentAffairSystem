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
'''
from TF import getTF, readData
from SimpleClassify import writeData


def saveDictAsTxt(filename, dataDict):
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
    posDict = normalization(getTF(1))
    # print(posDict.items())
    sumDict = normalization(getTF(2))
    # print(sumDict.items())
    returnDict = {}
    for key in posDict:
        try:
            temp = posDict[key] - sumDict[key]
            returnDict[key] = temp
            # tempStr = str(key) + ':' + str(returnDict[key]) + '\n'
            # retrunStr += tempStr
        except KeyError:
            continue
    saveDictAsTxt('pos.txt', posDict)
    saveDictAsTxt('sum.txt', sumDict)
    saveDictAsTxt('rt.txt', returnDict)
    # print(returnDict.items())
    # posStr = str(posDict) + '\n'
    # sumStr = str(sumDict) + '\n'
    #
    # f = open('pos.txt', 'w+', encoding='utf-8')
    # g = open('neg.txt', 'w+', encoding='utf-8')
    # h = open('rt.txt', 'w+', encoding='utf-8')
    # f.write(posStr)
    # g.write(sumStr)
    # h.write(retrunStr)
    # f.close()
    # g.close()
    # h.close()
    return dict(returnDict)


if __name__ == '__main__':
    # testDict = getTF(1)
    # normalization(testDict)
    # testDict2 = getTF(2)
    # print(testDict2)
    # normalization(testDict2)
    finalDict = imTFandIDF()
    fianl = sorted(finalDict.items(), key=lambda e: e[1], reverse=True)
    print(fianl)
    # saveDictAsTxt('最后结果.txt', fianl)
'''
改良思考
我们是否可以将相关评论作为TF的统计
将相关+不相关作为IDF的统计
但是这样的话相关系数就会发生变化,需要另外寻找相关系数

这里将TF 与 IDF 归一化
同时将原来的TF*IDF的方式改为TF-IDF的方式
排除掉了多个高频项的影响
'''
