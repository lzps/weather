#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from time import ctime
__author__ = 'L'


class forecast(object):
    """API说明：https://developer.forecast.io/docs/v2"""

    def __init__(self, key, location):
        """key即https://developer.forecast.io/ 的APIKEY
        location即经纬度，注意纬度在前经度在后。"""
        self.key = key
        self.loc = location
        self.data = requests.get('https://api.forecast.io/forecast/{0}/{1}?lang=zh&units=si'.format(key, location)).json()

    def now(self):
        """以字典形式返回实时天气状况"""
        t = str(self.data['currently'])
        a = ['precipIntensity', 'temperature', 'apparentTemperature', 'time', 'dewPoint', 'cloudCover', 'humidity', 'icon', 'ozone', 'precipProbability', 'pressure', 'windBearing', 'windSpeed', 'summary', 'precipType']
        b = ['降雨强度', '温度', '湿度', '数据更新时间', '露点', '云量', '湿度', '图标', '臭氧', '降雨概率', '气压', '风向', '风速', '摘要', '降雨类型']
        #https://zh.wikipedia.org/zh-cn/露点
        for i in range(0, len(a)):
            t = t.replace(a[i], b[i])
        infon = eval(t)
        infon['数据更新时间'] = ctime(infon['数据更新时间'])
        return infon


if __name__ == '__main__':
    from pprint import pprint
    t = forecast(input('请输入key：'), input('请输入经纬度（注意纬度在前经度在后）：'))
    pprint(t.now())
