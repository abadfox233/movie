# -*- coding: utf-8 -*-
# Created by Acer on 2018/1/31

from urllib.parse import urljoin
import re

from bs4 import BeautifulSoup


def prase_movie_list(base_url, html, movie_list, large):
    '''
    解析列表页 返回 影片信息
    :param base_url:
    :param html:
    :param movie_list:
    :param large:
    :return:
    '''
    pattern = re.compile('共\s*(\d+)\s*頁')
    soup = BeautifulSoup(html, 'lxml')
    div_list = soup.select('div[class="c cl"] a[class="z"]')
    for div in div_list:
        url = div['href']
        movie_list.append([div['title'], urljoin(base_url, url)])
    if large:
        large_num_label = soup.select('div[class="pg"] label span')
        try:
            if large_num_label:
                large_num = large_num_label[0]['title']
                large_result = pattern.findall(large_num)
                if large_result:
                    return large_result[0]
                else:
                    print('not found')
        except IndexError:
            print('未找到最大目录')
    else:
        return None


def get_movie_list(session, base_url, movie_list, large=False):
    movie_list.clear()
    try:
        result = session.get(base_url)
        print('[*] 当前网址 %s' % base_url)
        if result.status_code == 200:
            return prase_movie_list(base_url, result.text, movie_list, large)
    except IndexError:
        print('error')
