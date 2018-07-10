# encoding: utf-8
import os
import re
"""
@version: ??
@author: WangNing
@license: GUN 
@contact: yogehaoren@gmail.com
@site: 
@software: PyCharm
@file: test.py
@time: 2018/7/9 23:10
"""

if __name__ == '__main__':
    pattern = re.compile('\d+')
    pattern.match('full')
    result = pattern.fullmatch('55')
    print(len(result))