#!/usr/bin/env python3
import hashlib
import random

import requests

'''
简单的在线翻译
使用百度API
前往http://api.fanyi.baidu.com/api/trans/product/index获取更多信息
'''


def baidu_fanyi(q: str, fro: str = 'auto', to: str = 'zh', timeout: int = 5):
    """
    调用百度翻译API实现在线翻译
    :param q:请求翻译query
    :param fro:翻译源语言，默认自动识别
    :param to:译文语言，默认zh
    :param timeout:设置超时时间，默认5秒
    :return:正常返回json格式数据，否则返回None
    """
    appid = ''  # fill in your app_id
    salt = str(random.random())
    key = ''  # fill in your key
    text = appid + q + salt + key
    md5 = hashlib.md5()
    md5.update(text.encode('UTF-8'))
    sign = md5.hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    argv = {
        'appid': appid,
        'salt': salt,
        'key': key,
        'sign': sign,
        'q': q,
        'from': fro,
        'to': to
    }
    try:
        r = requests.get(url, params=argv, timeout=timeout)
    except:
        return None
    return r.json()


if __name__ == '__main__':
    print(baidu_fanyi('apple')['trans_result'][0]['dst'])
