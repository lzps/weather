#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from time import ctime
__author__ = 'L'


Skycons = {
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


class caiyunapp(object):
    """API说明：http://wiki.swarma.net/index.php/彩云天气API/v2"""

    def __init__(self, key, location):
        """key即https://www.caiyunapp.com/dev_center/login.html 登录后的API密钥
        location即经纬度，注意纬度在前经度在后 e.g.:"39.93,116.40\""""
        self.key = key
        self.loc = ",".join(location.split(",")[::-1])
        self.data = requests.get(
            'https://api.caiyunapp.com/v2/{0}/{1}/forecast.json'.format(self.key, self.loc)).json()
        self.dnow = requests.get(
            'https://api.caiyunapp.com/v2/{0}/{1}/realtime.json'.format(self.key, self.loc)).json()

    def now(self):
        """以字典形式返回实时天气状况"""
        t = str(self.dnow['result'])
        t = t.replace(", 'status': 'ok'", "")
        t = t.replace("'status': 'ok', ", "")
        a = ['cloudrate', 'humidity', 'precipitation', 'skycon', 'wind', 'aqi', 'temperature', 'local', 'datasource', 'nearest', 'intensity', 'direction', 'speed', 'distance']
        b = ['云量', '相对湿度', '降水', '天气概况', '风', '空气质量指数', '温度', '本地的', '数据源', '最近的降水带', '强度', '风向', '风速', '距离']
        for i in range(0, len(a)):
            t = t.replace(a[i], b[i])
        infon = eval(t)
        infon['数据更新时间'] = ctime(self.dnow['server_time'])
        infon['天气概况'] = Skycons[infon['天气概况']]
        return infon


if __name__ == '__main__':
    from pprint import pprint
    t = caiyunapp(input('请输入key：'), input('请输入经纬度 例如：location=39.93,116.40 （注意纬度在前经度在后）'))
    pprint(t.now())
