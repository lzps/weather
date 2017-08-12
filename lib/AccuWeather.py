#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lib.Caiyunapp import windint2str
__author__ = 'L'
R = [3, 12, False]
# R = [5, 12, False]


class AccuWeather(object):
    """API说明：https://developer.accuweather.com/apis"""
    """http://apidoc.weathercn.com/developers/"""

    def __init__(self, key, location):
        """key 即 https://developer.accuweather.com/ 注册后的API密钥
        location即经纬度，注意纬度在前经度在后 e.g.:"39.93,116.40\""""

        def get(url):
            req = requests.get(url)
            if req.status_code == 200:
                return req
            elif req.status_code == 401:
                self.base = 'api.accuweather.com'
                req = requests.get(url.replace('dataservice', 'api'))
                if req.status_code == 200:
                    return req
            print('请求失败：' + str(req.json()))

        self.base = 'dataservice.accuweather.com'
        location = get('https://{2}/locations/v1/cities/geoposition/search.json?q={0}&apikey={1}'.format(
            location, key, self.base)).json()['Key']
        self.dnow = get('https://{2}/currentconditions/v1/{0}.json?apikey={1}&language=zh&details=true&metric=false'.format(
            location, key, self.base)).json()[0]
        self.dD = get('https://{0}/forecasts/v1/daily/5day/{1}?apikey={2}&details=true&metric=true&language=zh'.format(
            self.base, location, key)).json()

    def now(self):
        """以字符串形式返回实时天气状况"""
        def M(x): return str(x['Metric']['Value'])
        temperature = M(self.dnow['Temperature']) + 'ºC' + \
            '(室内体感：{0}ºC)'.format(M(self.dnow['RealFeelTemperatureShade']))
        humidity = '湿度：' + str(self.dnow['RelativeHumidity']) + '%'
        wind = windint2str(
            self.dnow['Wind']['Direction']['Degrees'], M(self.dnow['Wind']['Speed']))
        update_time = self.dnow['LocalObservationDateTime'][5:16]
        return '，'.join([update_time, temperature, humidity, wind])

    def daily(self):
        """以字符串形式返回天级别的预报状况，返回 R[0] 天数据"""
        description = self.dD['Headline']['Text']
        dD = self.dD['DailyForecasts']
        date = [x['Date'][5:10] for x in dD]
        T_max = [x['Temperature']['Maximum']['Value'] for x in dD]
        T_min = [x['Temperature']['Minimum']['Value'] for x in dD]
        temperature = ['{0}-{1}ºC'.format(x[0], x[1])
                       for x in zip(T_min, T_max)]
        aqi = ['AQI：' + str(x['AirAndPollen'][0]['Value']) for x in dD]
        day = ['\n  -白天：{0}，降水概率：{1}%'.format(
            x['Day']['LongPhrase'], x['Day']['PrecipitationProbability']) for x in dD]
        night = ['\n  -夜晚：{0}，降水概率：{1}%'.format(
            x['Night']['LongPhrase'], x['Night']['PrecipitationProbability']) for x in dD]
        temp = list(zip(date, temperature, aqi, day, night))[:R[0]]
        return '\n'.join(['，'.join(x) for x in temp])


if __name__ == '__main__':
    t = AccuWeather(input('请输入key：'), input(
        '请输入经纬度 例如：location=39.93,116.40 （注意纬度在前经度在后）'))
    print(t.dnow)
    print(t.data)
    while True:
        eval(input())
