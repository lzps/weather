#!/usr/bin/env python3
# -*- coding: utf-8 -*-；
# TODO: 缓存，选择性输出
import os
from lib.lib import lib_list

lib_list = lib_list()


def match(text, name):
    for x in text.splitlines():
        x = x.split(':')
        if name == x[0]:
            return x[1]


if os.path.exists("main.ini"):
    with open("main.ini", "r") as f:
        f = f.read().replace(' ', '')
        lib_list, location = match(f, 'lib_list').split(
            ','), match(f, 'location')
else:
    print("未检测到配置，请输入")
    print("1.输入 API Key(可留空，留空则跳过获取)")
    api, text = [], []
    for x in lib_list:
        key = input(' -请输入 {0} 的 API Key：'.format(x))
        text.append(x + ': ' + key)
        if key:
            api.append(x)
    text.append('lib_list: ' + ','.join(api))
    print("2.输入城市信息，必填 可参考 https://www.ipip.net/ip.html")
    text.append('location: ' + input(" -请输入纬度经度（示例：39.93,116.40）："))
    with open("main.ini", "w") as f:
        f.write("\n".join(text))
    exit("\n配置已存至./main.ini，请检查后重新运行。")

for x in lib_list:
    exec("from lib.{0} import {0}".format(x))
    exec("t = {0}('{1}', '{2}')".format(x, match(f, x), location))
    print(t.now())
    print(t.daily())
    print(x + "\n")
