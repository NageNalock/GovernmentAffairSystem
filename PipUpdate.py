#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/28 22:02
# @Author  : Daisy
# @Site    : 
# @File    : PipUpdate.py
# @Software: PyCharm Community Edition

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)