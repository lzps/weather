#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from re import sub
import requests
__author__ = 'L'


'''d={
    0:["晴","Sunny"],
    1:["晴","Clear"],
    2:["晴","Fair"],
    3:["晴","Fair"],
    4:["多云","Cloudy"],
    5:["晴间多云","Partly Cloudy"],
    6:["晴间多云","Partly Cloudy"],
    7:["大部多云","Mostly Cloudy"],
    8:["大部多云","Mostly Cloudy"],
    9:["阴","Overcast"],
    10:["阵雨","Shower"],
    11:["雷阵雨","Thundershower"],
    12:["雷阵雨伴有冰雹","Thundershower with Hail"],
    13:["小雨","Light Rain"],
    14:["中雨","Moderate Rain"],
    15:["大雨","Heavy Rain"],
    16:["暴雨","Storm"],
    17:["大暴雨","Heavy Storm"],
    18:["特大暴雨","Severe Storm"],
    19:["冻雨","Ice Rain"],
    20:["雨夹雪","Sleet"],
    21:["阵雪","Snow Flurry"],
    22:["小雪","Light Snow"],
    23:["中雪","Moderate Snow"],
    24:["大雪","Heavy Snow"],
    25:["暴雪","Snowstorm"],
    26:["浮尘","Dust"],
    27:["扬沙","Sand"],
    28:["沙尘暴","Duststorm"],
    29:["强沙尘暴","Sandstorm"],
    30:["雾","Foggy"],
    31:["霾","Haze"],
    32:["风","Windy"],
    33:["大风","Blustery"],
    34:["飓风","Hurricane"],
    35:["热带风暴","Tropical Storm"],
    36:["龙卷风","Tornado"],
    37:["冷","Cold"],
    38:["热","Hot"],
    99:["未知","Unknown","未知"]
}#infon[int(now['now']['code'])'''


class Thinkpage(object):
    """API说明：http://www.thinkpage.cn/doc/v2"""

    def __init__(self, key, location):
        """key 即 http://www.thinkpage.cn/account 中账号资料的API密钥
        location即经纬度，注意纬度在前经度在后 e.g.:"39.93,116.40\""""
        self.key = key
        self.loc = location.replace(',', ':')
        self.dnow = requests.get(
            'https://api.thinkpage.cn/v2/weather/now.json?key={0}&city={1}'.format(self.key, self.loc)).json()
        self.data = requests.get(
            'https://api.thinkpage.cn/v2/weather/future.json?key={0}&city={1}'.format(self.key, self.loc)).json()
        # 可合并请求 all.json

    def now(self):
        """以字典形式返回实时天气状况"""
        t = str(self.dnow['weather'][0])
        a = ['last_update', 'temperature', 'city_name', 'now', 'air_quality', 'feels_like', 'humidity', 'visibility',
             'wind_direction', 'wind_scale', 'wind_speed', 'wind_direction_degree', 'pressure', '_rising', 'text']
        b = ['数据更新时间（该城市的本地时间）', '摄氏温度', '城市名', '实况', '空气质量', '体感温度',
             '相对湿度', '能见度', '风向', '风力等级', '风速', '风向角度', '气压', '升高', '天气现象']
        for i in range(0, len(a)):
            t = t.replace(a[i], b[i])
        infon = eval(t)
        del(infon['city_id'], infon['实况']['code'])
        return infon

    def daily(self):
        """以字典形式返回天级别的预报状况"""
        t = str(self.data['weather'][0])
        t = sub(r"'code1.*?,", '', t)
        t = sub(r"'code2.*?,", '', t)
        a = ['last_update', 'city_name', 'future',
             'date', 'text', 'high', 'low', 'wind', 'cop']
        b = ['数据更新时间（该城市的本地时间）', '城市名', '预报', '日期',
             '现象', '最高温度', '最低温度', '风况', '降水概率']
        for i in range(0, len(a)):
            t = t.replace(a[i], b[i])
        infon = eval(t)
        del(infon['city_id'])
        return infon


if __name__ == '__main__':
    from pprint import pprint
    t = Thinkpage(input('请输入key：'), input(
        '请输入经纬度 例如：location=39.93,116.40 （注意纬度在前经度在后）'))
    print(t.dnow)
    print(t.data)
    while True:
        eval(input())
