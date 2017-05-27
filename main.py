#!/usr/bin/env python3
# -*- coding: utf-8 -*-；
'''rem:
1. 代码需优化
2. caiyunapp skycon
'''

import os
from pprint import pprint

if os.path.exists("config"):
    with open("config","r") as f:
        f=f.read().splitlines()
        k=f[0].split(";")
        c=f[1].split(";")
else:
    print("未检测到配置，请输入\n")
    print("1.输入API Key(可留空，留空则跳过获取)")
    api=[]
    api.append("caiyunapp:"+input("请输入https://www.caiyunapp.com/dev_center/login.html 的API Key："))
    # api.append("forecast:"+input("请输入https://developer.forecast.io/ 的API Key："))
    api.append("thinkpage:"+input("请输入https://www.thinkpage.cn/doc 的API密钥："))
    print("\n2.输入城市信息，以下必填 可参考http://www.ipip.net/ip.html")
    with open("config","w") as f:
        f.write(";".join(api)+"\n"+input("请输入纬度经度（示例：39.93,116.40）："))
    exit("\n配置已存至./config，请检查后重新运行。")

for a in k:
    a = a.split(":")
    if a[1]:
        exec("from {0} import {0}".format(a[0]))
        exec("t = {0}('{1}', '{2}')".format(a[0], a[1], c[0]))
        pprint(t.now())
        pprint(t.daily())
        print(a[0] + "\n")
