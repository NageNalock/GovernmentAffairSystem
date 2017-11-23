#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 21:36
# @Author  : Daisy
# @Site    : 
# @File    : Test.py
# @Software: PyCharm Community Edition

from NLPTest import myAip
list = ['阿黄是条好狗','百度是一家伟大的公司']
# print(myAip())
result = myAip().commentTag(list)
print(result)