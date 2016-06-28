#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'L'

from time import ctime
import requests

Skycons={
    "CLEAR_DAY": "晴天",
    "CLEAR_NIGHT": "晴夜",
    "PARTLY_CLOUDY_DAY": "多云",
    "PARTLY_CLOUDY_NIGHT": "多云",
    "CLOUDY": "阴",
    "RAIN": "雨",
    "SLEET": "冻雨",
    "SNOW": "雪",
    "WIND": "风",
    "FOG": "雾",
    "HAZE": "霾"}

class caiyun(object):
    '''API说明：http://wiki.swarma.net/index.php/%E5%BD%A9%E4%BA%91%E5%A4%A9%E6%B0%94API/v2'''
    def __init__(self, key, location):
        '''key即https://www.caiyunapp.com/dev_center/login.html 登录后的API密钥
        location即经纬度，注意经度在前纬度在后。e.g.:"116.40,39.93"'''
        self.key = key
        self.loc = location
    
    def now(self):
        '''获取实时天气状况至infoN'''
        now = requests.get('https://api.caiyunapp.com/v2/{k}/{loc}/realtime.json'.format(k = self.key, loc = self.loc)).json()
        t = str(now['result'])
        t = t.replace(", 'status': 'ok'","")
        a = ['cloudrate', 'humidity', 'precipitation', 'skycon', 'wind']
        b = ['云量', '相对湿度', '降水', '天气概况', '风']
        i = 0
        while i<5:
            t = t.replace(a[i],b[i])
            i = i + 1
        infon = eval(t)
        infon['数据更新时间'] = ctime(now["server_time"])
        self.infoN = infon


if __name__=='__main__':
    from pprint import pprint
    t = caiyun(input('请输入key：'), input('请输入经纬度 例如：location=116.40,39.93（注意经度在前纬度在后）'))
    t.now()
    pprint(t.infoN)
