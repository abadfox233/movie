# encoding: utf-8
import hashlib
import MySQLdb
import requests
import os
"""
@version: 1.0
@author: WangNing
@license: GUN 
@contact: yogehaoren@gmail.com
@site: 
@software: PyCharm
@file: util.py
@time: 2018/7/10 23:25
@describe: 
"""
user = '52av'
passwd = '52av'
database = '52av'
conn = MySQLdb.connect("localhost", user, passwd, database, charset='utf8', use_unicode=True)
cursor = conn.cursor()


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def insert_to_mysql(parmars):
    if parmars[3] == 'None':
        image_path = download_image(parmars[2], parmars[5])
        if image_path:
            parmars = list(parmars)
            parmars[3] = image_path
            parmars = tuple(parmars)
    sql = 'INSERT INTO `52av`.`movie` ' \
          '(`title`, `movie_url`, `image_url`, `image_path`, `issue_time`, `movie_object_id`, `video_url`) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE movie_url=values(movie_url)'
    cursor.execute(sql, parmars)
    conn.commit()


def download_image(url, name):
    image_path = './image/{}.jpg'.format(name)
    response = requests.get(url)
    if not os.path.exists(image_path):
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                file.write(response.content)
        response.close()
    return image_path


def query_from_sql(movie_object_id):
    sql = 'select video_url, title from movie where movie_object_id = %s '
    cursor.execute(sql, (movie_object_id, ))
    data = cursor.fetchone()
    if data:
        return data[0]
    else:
        return None
    # return conn.commit()


if __name__ == '__main__':
    print(query_from_sql('005ed038858f98c58a5a666fc9f585b'))