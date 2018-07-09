# -*- coding: utf-8 -*-
# Created by Acer on 2018/1/31

import requests
import os

from movie_list import get_movie_list
from download import download_movie
from get_video import get_m3u8_url

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}

large = 330
session = requests.Session()
session.headers = header
proxies = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
session.proxies = proxies
base_url = 'http://www.52av.tv/forum.php?mod=forumdisplay&fid=67&filter=typeid&typeid=128'
now_page = 0


def get_page_url():
    if now_page != 0:
        return base_url+'&page='+str(now_page)
    else:
        return base_url


def print_movie_list(movie_list):
    '''
    打印影片列表
    :param movie_list:
    :return:
    '''
    for i in range(len(movie_list)):
        print(i, ':', movie_list[i][0])
    print('[*] 当前页面', now_page, '  共', large, '页')


def init_env_environment():
    '''
    初始化环境 创建 m3u8 output video 文件夹
    :return:
    '''
    dirs = ['output', 'm3u8', 'video']
    for path in dirs:
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkdir(path)
        if path == 'video':
            all_file = [os.path.abspath('./video/' + path) for path in os.listdir(path)]
            for file in all_file:
                os.remove(file)
    if os.path.exists('error.txt'):
        os.remove('error.txt')
    print('[*] 环境初始化成功!')


if __name__ == '__main__':
    print('***************** 欢迎 进入 *****************')
    init_env_environment()
    movie_list = []
    large = get_movie_list(session, get_page_url(), movie_list, True)
    print_movie_list(movie_list)
    while True:
        print('[*] 输入(q)： 退出 ** 输入(数字)： 获取相应影片 ** 输入(p)： 跳转页面 ** 输入(n)：下一页')
        cmd = input('[>] 请输入：')
        if cmd == 'q':
            print('[!] Bye!')
            break
        elif cmd == 'n':
            now_page += 1
            large = get_movie_list(session, get_page_url(), movie_list, True)
            print_movie_list(movie_list)
        elif cmd == 'p':
            page_num = input('[>] 请输入页数：')
            if page_num.isnumeric():
                now_page = page_num
                large = get_movie_list(session, get_page_url(), movie_list, True)
                print_movie_list(movie_list)
            else:
                print('[!] 输入不合法！ 请重新输入')
        elif cmd.isnumeric():
            print('[*] 正在获取影片链接 请耐心等待(2min)')
            m3u8_url = get_m3u8_url(session, movie_list[int(cmd)][1])
            if m3u8_url:
                print('[*] 获取成功 ', m3u8_url)
                download_movie(m3u8_url, movie_list[int(cmd)][0])
            else:
                print("[!] 获取失败请更换资源或重新尝试!")
        else:
            print('[!] 输入不合法！ 请重新输入')
