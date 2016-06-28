#!/usr/bin/env python3
# -*- coding: utf-8 -*-；
#bug:cn文件有bug；初次使用多了一次请求
#To do:多城市；ip检测城市；wego

import requests,os
from pprint import pprint

'''
ip=json.loads(requests.get('http://ipinfo.io').text)['ip']
city=json.loads(requests.get('http://ip.taobao.com/service/getIpInfo.php?ip='+ip).text)['data']['city']
t=json.loads(requests.get('http://freeapi.ipip.net/'+ip).text)[2]
'''

if os.path.exists('key'):
    with open('key','r') as f:
        k=f.read().split(',')
else:
    a='True,'
    k1=input('请输入http://www.heweather.com/my/service的个人认证key：')
    k2=input('请输入https://developer.forecast.io/的API Key(可选)：')
    if k1=='':
        print('Bug!')
        exit(input('Press any key to exit . . .'))
    else:
        if k2=='':
            a='False,'
        with open('key','w') as f:
            f.write(a+k1+','+k2)

if os.path.exists('city'):
    with open('city','r') as f:
        c=f.read().split(',')
else:
    with open('cn','rb') as f:
        f = eval(f.read().decode('utf-8'))
    city = input('请输入城市拼音：')
    if city in f:
        a = requests.get('https://api.heweather.com/x3/weather?city={c}&key={k}'.format(c=city,k=k[1])).json()['HeWeather data service 3.0'][0]
        with open('city','w') as f:
            f.write(city+','+a['basic']['lat']+','+a['basic']['lon'])
    else:
        if city=='':
            pass
        else:
            for a in f.keys():
                if city in a:
                    print(a)
        print('\n请重新输入！')
        exit(input('Press any key to exit . . .'))

pprint(requests.get('https://api.heweather.com/x3/weather?city={c}&key={k}'.format(c=c[0],k=k[1])).json()['HeWeather data service 3.0'][0])

if eval(k[0]):
	a=requests.get('https://api.forecast.io/forecast/{k}/{c1},{c2}?lang=zh'.format(k=k[2],c1=c[1],c2=c[2])).json()
	pprint(a)
	while True:
		eval(input(''))