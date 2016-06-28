#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'L'

import requests
from time import ctime

class forecast(object):
    '''API说明：https://developer.forecast.io/docs/v2'''
    def __init__(self, key, location):
        '''key即https://developer.forecast.io/ 的APIKEY
        location即经纬度，注意纬度在前经度在后。'''
        self.key = key
        self.loc = location
        self.data = requests.get('https://api.forecast.io/forecast/{0}/{1}?lang=zh'.format(key, location)).json()
    
    def now(self):
        '''得到实时天气状况至infoN'''
        t = str(self.data['currently'])
        a = ['precipIntensity', 'temperature', 'apparentTemperature', 'time']
        b = ['降雨强度', '温度', '湿度', '数据更新时间']
        for i in range(0, len(a)):
            t = t.replace(a[i],b[i])
        infon = eval(t)
        infon['数据更新时间'] = ctime(infon['数据更新时间'])
        self.infoN = infon


if __name__=='__main__':
    from pprint import pprint
    t = forecast(input('请输入key：'), input('请输入经纬度（注意纬度在前经度在后）：'))
    t.now()
    pprint(t.infoN)
