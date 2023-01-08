import requests
import re
import json


def get_url(song_url):
    if re.match('https?://kg.qq.com/', song_url) is None:
        return '不是有效的链接'
    try:
        resp = requests.get(url=song_url)
    except:
        return '爬取失败'
    res = re.search('({"shareid":".*); </script>', resp.text)
    if res is None:
        return '爬取失败'
    else:
        data_json = json.loads(res.group(1))
        return data_json['detail']['playurl']


if __name__ == '__main__':
    pass