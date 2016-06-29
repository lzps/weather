# Weather
遵循MIT许可证

这是一个python3的脚本，用于查询天气。使用时直接运行main.py

首次运行将提示输入API KEY与经纬度

# Demo
```
$ python3 ./main.py
未检测到配置，请输入

1.输入API Key(可留空，留空则跳过获取)
请输入https://www.caiyunapp.com/dev_center/login.html 的API Key：xxx
请输入https://developer.forecast.io/ 的API Key：xxx
请输入https://www.thinkpage.cn/doc 的API密钥：xxx

2.输入城市信息，以下必填 可参考http://www.ipip.net/ip.html
请输入纬度经度（示例：39.93,116.40）：39.93,116.40
配置已存至./config，请检查后重新运行。

$ python3 ./main.py
{'pm25': 133.0,
 '云量': 0.04,
 '天气概况': '晴夜',
 '数据更新时间': 'Wed Jun 29 22:00:35 2016',
 '温度': 24.0,
 '相对湿度': 0.72,
 '空气质量指数': 176.0,
 '降水': {'最近的降水带': {'强度': 0.25, '距离': 21.43},
        '本地的': {'强度': 0.0, '数据源': 'radar'}},
 '风': {'风向': 194.21, '风速': 7.06}}
caiyunapp

{'云量': 0.06,
 '图标': 'clear-night',
 '摘要': '晴朗',
 '数据更新时间': 'Wed Jun 29 22:03:39 2016',
 '气压': 1003.38,
 '温度': 21.46,
 '湿度': 21.46,
 '臭氧': 330.51,
 '降雨强度': 0.061,
 '降雨概率': 0.07,
 '降雨类型': 'rain',
 '露点': 16.67,
 '风向': 190,
 '风速': 1.83}
forecast

{'城市名': '北京',
 '实况': {'体感温度': '24',
        '天气现象': '多云',
        '摄氏温度': '24',
        '气压': '998',
        '气压升高': '未知',
        '相对湿度': '82',
        '空气质量': None,
        '能见度': '1.7',
        '风力等级': '1',
        '风向': '北',
        '风速': '2.16'},
 '数据更新时间（该城市的本地时间）': '2016-06-29T21:45:00+08:00'}
thinkpage

```


# 需求
安装python3，pip安装requests

## ubuntu 16.04 LTS
```
sudo apt-get install python3
sudo pip3 install requests
git clone https://github.com/lzps/weather.git
cd weather/
python3 ./main.py
```
