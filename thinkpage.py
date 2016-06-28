#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'L'

import requests

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
    35:[" 热带风暴","Tropical Storm"],
    36:["龙卷风","Tornado"],
    37:["冷","Cold"],
    38:["热","Hot"],
    99:["未知","Unknown","未知"]
}#d[int(now['now']['code'])'''

class thinkpage(object):
    '''API说明：http://www.thinkpage.cn/doc'''
    def __init__(self, key, location):
        '''key即http://www.thinkpage.cn/account 中账号资料的API密钥
        location即经纬度，注意纬度在前经度在后 e.g.:"39.93,116.40"'''
        self.key = key
        self.loc = location
    
    def now(self):
        '''获取天气实况至infoN'''
        now = requests.get('https://api.thinkpage.cn/v3/weather/now.json?key={k}&location={loc}'.format(k = self.key, loc = self.loc.replace(',',':'))).json()['results'][0]
        infon = {}
        infon['last_update'] = '数据更新时间（该城市的本地时间）：' + now['last_update']
        infon['weather'] = now['location']['name'] + '天气概况：' + now['now']['text']
        infon['temperature'] = '摄氏温度：' + now['now']['temperature']
        self.infoN = infon


if __name__=='__main__':
    from pprint import pprint
    t = thinkpage(input('请输入key：'), input('请输入经纬度 例如：location=39.93,116.40 （注意纬度在前经度在后）'))
    t.now()
    pprint(t.infoN)
