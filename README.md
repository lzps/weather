# Weather
遵循MIT许可证

这是一个python3的脚本，用于查询天气。使用时直接运行main.py，也可单独运行其它文件调试。

首次运行将提示输入API KEY与经纬度

# Demo
```
$ python3 ./main.py
未检测到配置，请输入

1.输入API Key(可留空，留空则跳过获取)
请输入https://www.caiyunapp.com/dev_center/login.html 的API Key：xxx
请输入https://www.thinkpage.cn/doc 的API密钥：xxx

2.输入城市信息，以下必填 可参考http://www.ipip.net/ip.html
请输入纬度经度（示例：39.93,116.40）：39.93,116.40
配置已存至./config，请检查后重新运行。

$ python3 ./main.py
{'pm25': 80.0,
 '云量': 0.01,
 '天气概况': '晴天',
 '数据更新时间': 'Sat May 27 16:38:25 2017',
 '温度': 30.0,
 '相对湿度': 0.2,
 '空气质量指数': 107.0,
 '降水': {'最近的降水带': {'强度': 0.25, '距离': 34.46},
        '本地的': {'强度': 0.0, '数据源': 'radar'}},
 '风': {'风向': 201.76, '风速': 10.68}}
{'aqi': [{'平均': 129.0, '日期': '2017-05-27', '最低': 52.0, '最高': 150.0},
         {'平均': 121.67, '日期': '2017-05-28', '最低': 72.0, '最高': 196.0},
         {'平均': 81.71, '日期': '2017-05-29', '最低': 68.0, '最高': 105.0},
         {'平均': 92.25, '日期': '2017-05-30', '最低': 72.0, '最高': 121.0},
         {'平均': 140.38, '日期': '2017-05-31', '最低': 119.0, '最高': 171.0}],
 'pm25': [{'平均': 96.5, '日期': '2017-05-27', '最低': 36.0, '最高': 115.0},
          {'平均': 90.83, '日期': '2017-05-28', '最低': 52.0, '最高': 147.0},
          {'平均': 60.12, '日期': '2017-05-29', '最低': 49.0, '最高': 78.0},
          {'平均': 68.42, '日期': '2017-05-30', '最低': 52.0, '最高': 91.0},
          {'平均': 106.33, '日期': '2017-05-31', '最低': 90.0, '最高': 129.0}],
 'skycon': [{'value': 'CLEAR_DAY', '日期': '2017-05-27'},
            {'value': 'PARTLY_CLOUDY_DAY', '日期': '2017-05-28'},
            {'value': 'RAIN', '日期': '2017-05-29'},
            {'value': 'RAIN', '日期': '2017-05-30'},
            {'value': 'PARTLY_CLOUDY_DAY', '日期': '2017-05-31'}],
 '云量': [{'平均': 0.07, '日期': '2017-05-27', '最低': 0.0, '最高': 0.27},
        {'平均': 0.41, '日期': '2017-05-28', '最低': 0.0, '最高': 1.0},
        {'平均': 0.94, '日期': '2017-05-29', '最低': 0.86, '最高': 1.0},
        {'平均': 0.89, '日期': '2017-05-30', '最低': 0.22, '最高': 1.0},
        {'平均': 0.24, '日期': '2017-05-31', '最低': 0.0, '最高': 0.99}],
 '感冒风险': [{'介绍': '极易发', '指数': '4', '日期时间': '2017-05-27'},
          {'介绍': '极易发', '指数': '4', '日期时间': '2017-05-28'},
          {'介绍': '极易发', '指数': '4', '日期时间': '2017-05-29'},
          {'介绍': '极易发', '指数': '4', '日期时间': '2017-05-30'},
          {'介绍': '极易发', '指数': '4', '日期时间': '2017-05-31'}],
 '日出日落': [{'日出时间': {'时间': '04:50'},
           '日期': '2017-05-27',
           '日落时间': {'时间': '19:32'}},
          {'日出时间': {'时间': '04:49'},
           '日期': '2017-05-28',
           '日落时间': {'时间': '19:33'}},
          {'日出时间': {'时间': '04:49'},
           '日期': '2017-05-29',
           '日落时间': {'时间': '19:34'}},
          {'日出时间': {'时间': '04:48'},
           '日期': '2017-05-30',
           '日落时间': {'时间': '19:35'}},
          {'日出时间': {'时间': '04:48'},
           '日期': '2017-05-31',
           '日落时间': {'时间': '19:35'}}],
 '洗车指数': [{'介绍': '较适宜', '指数': '2', '日期时间': '2017-05-27'},
          {'介绍': '较不适宜', '指数': '3', '日期时间': '2017-05-28'},
          {'介绍': '较不适宜', '指数': '3', '日期时间': '2017-05-29'},
          {'介绍': '较不适宜', '指数': '3', '日期时间': '2017-05-30'},
          {'介绍': '较适宜', '指数': '2', '日期时间': '2017-05-31'}],
 '温度': [{'平均': 28.38, '日期': '2017-05-27', '最低': 17.0, '最高': 33.0},
        {'平均': 29.01, '日期': '2017-05-28', '最低': 21.0, '最高': 36.0},
        {'平均': 23.62, '日期': '2017-05-29', '最低': 19.0, '最高': 29.0},
        {'平均': 22.52, '日期': '2017-05-30', '最低': 18.0, '最高': 30.0},
        {'平均': 25.0, '日期': '2017-05-31', '最低': 18.0, '最高': 32.0}],
 '相对湿度': [{'平均': 0.32, '日期': '2017-05-27', '最低': 0.19, '最高': 0.6},
          {'平均': 0.35, '日期': '2017-05-28', '最低': 0.13, '最高': 0.7},
          {'平均': 0.32, '日期': '2017-05-29', '最低': 0.24, '最高': 0.55},
          {'平均': 0.73, '日期': '2017-05-30', '最低': 0.51, '最高': 0.88},
          {'平均': 0.44, '日期': '2017-05-31', '最低': 0.14, '最高': 0.9}],
 '着装指数': [{'介绍': '很热', '指数': '2', '日期时间': '2017-05-27'},
          {'介绍': '很热', '指数': '2', '日期时间': '2017-05-28'},
          {'介绍': '热', '指数': '3', '日期时间': '2017-05-29'},
          {'介绍': '热', '指数': '3', '日期时间': '2017-05-30'},
          {'介绍': '热', '指数': '3', '日期时间': '2017-05-31'}],
 '紫外线': [{'介绍': '强', '指数': '4', '日期时间': '2017-05-27'},
         {'介绍': '强', '指数': '4', '日期时间': '2017-05-28'},
         {'介绍': '最弱', '指数': '1', '日期时间': '2017-05-29'},
         {'介绍': '最弱', '指数': '1', '日期时间': '2017-05-30'},
         {'介绍': '中等', '指数': '3', '日期时间': '2017-05-31'}],
 '降雨强度': [{'平均': 0.0, '日期': '2017-05-27', '最低': 0.0, '最高': 0.0},
          {'平均': 0.0019, '日期': '2017-05-28', '最低': 0.0, '最高': 0.0446},
          {'平均': 0.0793, '日期': '2017-05-29', '最低': 0.0, '最高': 0.3588},
          {'平均': 0.6814, '日期': '2017-05-30', '最低': 0.0, '最高': 1.7954},
          {'平均': 0.0, '日期': '2017-05-31', '最低': 0.0, '最高': 0.0}],
 '风况': [{'平均': {'风力': 9.1, '风向': 111.57},
         '日期': '2017-05-27',
         '最低': {'风力': 7.18, '风向': 146.33},
         '最高': {'风力': 11.4, '风向': 97.0}},
        {'平均': {'风力': 13.87, '风向': 70.35},
         '日期': '2017-05-28',
         '最低': {'风力': 3.94, '风向': 122.39},
         '最高': {'风力': 26.0, '风向': 38.87}},
        {'平均': {'风力': 9.12, '风向': 112.72},
         '日期': '2017-05-29',
         '最低': {'风力': 1.64, '风向': 243.01},
         '最高': {'风力': 19.69, '风向': 108.59}},
        {'平均': {'风力': 6.85, '风向': 193.5},
         '日期': '2017-05-30',
         '最低': {'风力': 1.49, '风向': 92.41},
         '最高': {'风力': 11.58, '风向': 193.32}},
        {'平均': {'风力': 8.85, '风向': 200.57},
         '日期': '2017-05-31',
         '最低': {'风力': 1.16, '风向': 130.35},
         '最高': {'风力': 17.5, '风向': 197.67}}]}
caiyunapp

{'城市名': '北京',
 '实况': {'体感温度': '29',
        '天气现象': '晴',
        '摄氏温度': '30',
        '气压': '998',
        '气压升高': '未知',
        '相对湿度': '38',
        '空气质量': None,
        '能见度': '8.4',
        '风力等级': '2',
        '风向': '西南',
        '风速': '8.64'},
 '数据更新时间（该城市的本地时间）': '2017-05-27T15:35:00+08:00'}
{'城市名': '北京',
 '数据更新时间（该城市的本地时间）': '2017-05-27T11:00:00+08:00',
 '预报': [{'day': '周六',
         '日期': '2017-05-27',
         '最低温度': '21',
         '最高温度': '34',
         '现象': '晴',
         '降水概率': '',
         '风况': '西南风3级'},
        {'day': '周日',
         '日期': '2017-05-28',
         '最低温度': '21',
         '最高温度': '36',
         '现象': '多云/阴',
         '降水概率': '',
         '风况': '北风4级'},
        {'day': '周一',
         '日期': '2017-05-29',
         '最低温度': '18',
         '最高温度': '29',
         '现象': '阴/阵雨',
         '降水概率': '',
         '风况': '东风3级'}]}
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
