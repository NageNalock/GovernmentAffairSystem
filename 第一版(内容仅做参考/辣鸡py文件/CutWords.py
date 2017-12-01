#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 20:28
# @Author  : Daisy
# @Site    : 
# @File    : CutWords.py
# @Software: PyCharm Community Edition
'''
对相关微博进行分词同时去停用词
并用卡方统计的方式提取关键词
再对关键词进行保存
'''
import jieba
import csv
import re
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.metrics import BigramAssocMeasures


def getRegularDataWords(filename):
    #  先进行正则表达式 再分词
    fileName = '分表/' + filename + '.csv'
    stopWords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
    str = []
    with open(fileName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            row['微博内容'] = (row['微博内容']).strip().rstrip(' ')
            #  正则表达式 只保留汉字
            pattern = re.compile(r'[\u4e00-\u9fa5]+')
            filterdata = re.findall(pattern, row['微博内容'])
            cleanedData = ''.join(filterdata)
            seg = jieba.cut(cleanedData, cut_all=False)  # 精准模式

            str.append((list(set(seg) - set(stopWords) - set('\n'))))
    f.close()
    return str


def getPosDataWords(filename):
    fileName = '分表/' + filename + '.csv'
    stopWords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
    str = []
    with open(fileName, 'r', encoding='utf-8') as f:
        data_csv = csv.DictReader(f)
        for row in data_csv:
            row['微博内容'] = (row['微博内容']).strip().rstrip(' ')
            seg = jieba.cut(row['微博内容'], cut_all=False)  # 精准模式

            str.append((list(set(seg) - set(stopWords) - set('\n'))))
    f.close()
    return str


def jieba_words_feature(num=2400):  # num为特征维度
    # print('结巴分词')
    pos_words = []
    neg_words = []
    # 将分词完成后的词语分类存进集合
    for words in getRegularDataWords('pos'):
        for word in words:
            pos_words.append(word)
    for words in getRegularDataWords('neg'):
        for word in words:
            neg_words.append(word)

    # 用FreqDist来表示单词的整体频率，ConditionalFreqDist的条件是类别标签
    word_f = FreqDist()  # FreDist()构建出一个词为key,词频为value,按词频由大到小排列
    both_word_f = ConditionalFreqDist()
    for word in pos_words:
        word_f[word] += 1
        both_word_f['pos'][word] += 1
        # print('pos:', word_f[word])
    # print(both_word_f.N())
    for word in neg_words:
        word_f[word] += 1
        both_word_f['neg'][word] += 1
        # print('neg:', word_f[word])
    # print(word_f.items())
    # print(both_word_f.N())

    pos_words_num = both_word_f['pos'].N()
    neg_words_num = both_word_f['neg'].N()
    words_num = pos_words_num + neg_words_num

    # 用BigramAssocMeasures.chi_sq函数(卡方)为词汇计算评分，然后按分数排序，放入一个集合里
    word_scores = {}
    for word, freq in word_f.items():
        pos_score = BigramAssocMeasures.chi_sq(both_word_f['pos'][word], (freq, pos_words_num), words_num)
        # print('pos:', pos_score)
        neg_score = BigramAssocMeasures.chi_sq(both_word_f['neg'][word], (freq, neg_words_num), words_num)
        word_scores[word] = pos_score + neg_score  # 该词语总信息量

    best_vals = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)[:num]  # 倒叙排序
    best_words = set([w for w, s in best_vals])
    print(best_words)

    h = open('feature.txt', 'w+', encoding='utf-8')
    h.write(str(best_words))
    h.close()


if __name__ == '__main__':
    '''
    两个文件名 neg pos
    '''
    jieba_words_feature()
