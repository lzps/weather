#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'http://www.heweather.com/my/service'

__author__ = 'L'

def infoH(geo):
a = requests.get('https://api.heweather.com/x3/weather?city={c}&key={k}'.format(c=c[0],k=k[1])).json()['HeWeather data service 3.0'][0]
