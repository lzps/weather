#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import localtime
from time import strftime
import requests
__author__ = 'L'

R = [5, 12, False]
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


class Caiyunapp(object):
    """API说明：http://wiki.swarma.net/index.php/彩云天气API/v2"""

    def __init__(self, key, location):
        """key 即 https://www.caiyunapp.com/dev_center/login.html 登录后的API密钥
        location即经纬度，注意纬度在前经度在后 e.g.:"39.93,116.40\""""
        loc = ",".join(location.split(",")[::-1])
        self.data = requests.get(
            'https://api.caiyunapp.com/v2/{0}/{1}/forecast?lang=zh_CN&unit=metric'.format(key, loc)).json()
        self.dnow = requests.get(
            'https://api.caiyunapp.com/v2/{0}/{1}/realtime?lang=zh_CN&unit=metric'.format(key, loc)).json()

    def now(self):
        """以字符串形式返回实时天气状况"""
        """可添加云量、降水等信息"""
        temperature = str(self.dnow['result']['temperature']) + 'ºC'
        aqi = 'AQI：' + str(self.dnow['result']['aqi'])
        humidity = '湿度：' + \
            str(float(self.dnow['result']['humidity'])
                * 100).replace('.0', '%')
        wind = windint2str(
            self.dnow['result']['wind']['direction'], self.dnow['result']['wind']['speed'])
        update_time = strftime(
            '%m-%dT%H:%M', localtime(self.dnow['server_time']))
        return '，'.join([update_time, temperature, humidity, aqi, wind])

    def daily(self):
        """以字符串形式返回天级别的预报状况，返回 R[0] 天数据"""
        """可添加云量、AQI、日出日落、风等信息"""
        temp = self.data['result']['daily']['temperature']
        date = [x['date'][5:] for x in temp]
        T_max = [x['max'] for x in temp]
        T_min = [x['min'] for x in temp]
        temperature = ['{0}-{1}ºC'.format(x[0], x[1])
                       for x in zip(T_min, T_max)]
        skycon = [Skycons[x['value']]
                  for x in self.data['result']['daily']['skycon']]
        intensity = ['日均降雨强度：' + str(x['avg'])
                     for x in self.data['result']['daily']['precipitation']]
        temp = list(zip(date, temperature, skycon, intensity))[:R[0]]
        return '\n'.join(['，'.join(x) for x in temp])


def windint2str(direction, speed):
    '''
    direction： 正北方向为0度，顺时针增加到360度。
    参考：http://www.kepu.net.cn/gb/earth/weather/wind/wnd008_1.html
    speed： 风速，公里每小时。
    参考：https://zh.wikipedia.org/zh-cn/蒲福氏风级 修改了3,5,8,9级名称
    S = log(int(speed / 0.836), 1.5) - 1
    '''
    D = int((float(direction) + 22.5) // 45)
    S_R = [range(2), range(2, 6), range(6, 12), range(12, 19), range(19, 30), range(30, 40), range(
        40, 51), range(51, 62), range(62, 75), range(75, 87), range(87, 103), range(103, 117)]
    S = 12
    for i, x in enumerate(S_R):
        if int(float(speed)) in x:
            S = i
            break
    D_str = ['北', '东北', '东', '东南', '南', '西南', '西', '西北', '北']
    S_str = ['无', '软', '轻', '微', '和', '劲', '强', '疾', '大', '烈', '暴', '台', '飓']
    return '{0}风、{1}级{2}风'.format(D_str[D], str(S), S_str[S])


if __name__ == '__main__':
    t = Caiyunapp(input('请输入key：'), input(
        '请输入经纬度 例如：location=39.93,116.40 （注意纬度在前经度在后）'))
    print(t.dnow)
    print(t.data)
    while True:
        eval(input())
