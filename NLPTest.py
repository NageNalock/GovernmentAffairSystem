#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 10:15
# @Author  : Daisy
# @Site    : 
# @File    : NLPTest.py
# @Software: PyCharm Community Edition

from aip import AipNlp


def myAip():
    """ 你的 APPID AK SK """
    APP_ID = '10288634'
    API_KEY = '6lkpB5dBiMCcNRiU5MsPDGYu'
    SECRET_KEY = 'bkFssTaSQjEXPynFIjuytywOIREGzpGI'

    aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    print(aipNlp)
    return aipNlp


# def

if __name__ == '__main__':
    APP_ID = '10288634'
    API_KEY = '6lkpB5dBiMCcNRiU5MsPDGYu'
    SECRET_KEY = 'bkFssTaSQjEXPynFIjuytywOIREGzpGI'

    aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    print(aipNlp)
    # str1 = '【九寨沟县地震灾后首个校园应急示范站成立】“高新九寨心连心，震后九寨更美丽。”9月28日下午，由成都高新区志愿者协会党支部、成都市义工联合会党支部联合主办的“支援九寨沟县第四小学应急示范站建设暨校园信息建设项目”捐赠仪式在九寨沟县第四小学举行。捐赠活动上，由成都高新区志愿者协会援建'
    # str2 = '【四川表彰九寨沟地震及茂县山体滑坡抢险救灾先进典型丨全名单】“8·8”九寨沟地震及“6·24”茂县特大山体滑坡灾害发生后，在党中央、国务院和四川省委、省政府的坚强领导下，四川省各级党组织和广大共产党员勇于担当、冲锋在前，为抗震抢险救灾作出了重要贡献，涌现出一大批先进典型。'
    # str3 = '【汶川一小入选全国文明校园候选名单】9月27日，记者从中国文明网获悉，中央文明办公示了第一届全国文明校园候选名单。四川省22所学校入选，汶川县第一小学校上榜。记者了解到，创建期内学校领导班子成员有严重违纪、违法事件，有重大校园安全责任事故、重大消防责任事故，有严重违规办学(办班)等问题'
    # str4 = '#抗震救灾气象行动# 【南方大范围强降雨来袭 九寨沟震区有降雨】预计未来四天，贵州、广西及江南西部和北部、江汉、江淮、黄淮等地将先后出现大到暴雨、局地大暴雨，主要降水时段在11日夜间至13日；期间，华北等地将出现多雷阵雨天气。上述部分地区并伴有短时强降水、局地有雷暴大风等强对流天气。请公'
    # result1 = aipNlp.simnet(str1, str3, {'model': 'BOW'})
    # result2 = aipNlp.simnet(str4, str3)
    # print('相关评价', result1['score'])
    # # print('不相关评价', result2['score'])
    # # print('*****')
    # # result3 = myAip().simnet(str1,str3)
    # # print(result3)
