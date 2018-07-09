# encoding: utf-8
import os
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
    dirs = ['output', 'm3u8', 'video']
    for path in dirs:
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkdir(path)
        if path == 'video':
            all_file = [os.path.abspath('./video/'+path) for path in os.listdir(path)]
            for file in all_file:
                os.remove(file)