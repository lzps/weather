# Weather
遵循MIT许可证

这是一个python3的脚本，用于查询天气。使用时直接运行main.py

首次运行将提示输入API KEY与经纬度

# Demo
```
$ python3 ./main.py
未检测到配置，请输入

1.输入API Key(可留空，留空则跳过获取)
请输入https://www.caiyunapp.com/dev_center/login.html 的API Key：
请输入https://developer.forecast.io/ 的API Key：
请输入https://www.thinkpage.cn/doc 的API密钥：

2.输入城市信息，以下必填 可参考http://www.ipip.net/ip.html
请输入纬度经度（示例：39.93,116.40）：
配置已存至./config，请检查后重新运行。

$ python3 ./main.py
{'aqi': 182.0,
 'pm25': 137.0,
 'temperature': 24.0,
 '云量': 0.46,
 '天气概况': 'PARTLY_CLOUDY_DAY',
 '数据更新时间': 'Wed Jun 29 10:13:17 2016',
 '相对湿度': 0.66,
 '降水': {'local': {'datasource': 'radar', 'intensity': 0.0, 'status': 'ok'},
        'nearest': {'distance': 10000.0, 'intensity': 0.0, 'status': 'ok'}},
 '风': {'direction': 154.42, 'speed': 5.56}}
caiyunapp


{'cloudCover': 0.44,
 'dewPoint': 63.84,
 'humidity': 0.69,
 'icon': 'partly-cloudy-day',
 'ozone': 344.57,
 'precipProbability': 0.04,
 'precipType': 'rain',
 'pressure': 1004.8,
 'summary': '局部多云',
 'windBearing': 157,
 'windSpeed': 2.35,
 '数据更新时间': 'Wed Jun 29 09:52:27 2016',
 '温度': 74.89,
 '湿度': 74.89,
 '降雨强度': 0.0018}
forecast

{'last_update': '数据更新时间（该城市的本地时间）：2016-06-29T09:25:00+08:00',
 'temperature': '摄氏温度：23',
 'weather': '北京天气概况：雷阵雨'}
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
