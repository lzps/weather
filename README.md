# Weather

这是一个python3的脚本，用于查询天气。使用时直接运行main.py。

首次运行将提示输入API KEY与经纬度

注意；请使用 python3 运行，并安装 requests 库

遵循MIT许可证

## Demo

``` bash
$ python3 main.py
未检测到配置，请输入
1.输入 API Key(可留空，留空则跳过获取)
 -请输入 Caiyunapp 的 API Key：xxx
 -请输入 AccuWeather 的 API Key：3HthYWILGYnX5oKveX72Frvv7agCfw9Y
2.输入城市信息，必填 可参考 https://www.ipip.net/ip.html
 -请输入纬度经度（示例：39.93,116.40）：39.93,116.40

配置已存至./main.ini，请检查后重新运行。
$ python3 main.py
08-11T21:35，23.0ºC，湿度：42%，AQI：37.0，南风、3级微风
08-11，23.0-31.0ºC，雨，日均降雨强度：2.785
08-12，23.0-31.0ºC，雨，日均降雨强度：1.8399
08-13，22.0-26.0ºC，雨，日均降雨强度：0.8987
08-14，22.0-29.0ºC，多云，日均降雨强度：0.0
08-15，22.0-31.0ºC，晴天，日均降雨强度：0.0
Caiyunapp

08-11T21:20，22.2ºC(室内体感：19.4ºC)，湿度：88%，东风、4级和风
08-11，23.0-31.0ºC，AQI：79，
  -白天：局部地区有雷雨，降水概率：47%，
  -夜晚：间歇性降雨，降水概率：80%
08-12，22.0-31.0ºC，AQI：73，
  -白天：局部地区有雷雨，降水概率：61%，
  -夜晚：几场雷雨，降水概率：71%
08-13，23.0-29.0ºC，AQI：89，
  -白天：局部地区有雷雨，降水概率：40%，
  -夜晚：局部地区有雷雨，降水概率：43%
AccuWeather

```

## lib 说明

我使用过四种 API：[AccuWeather](https://developer.accuweather.com/packages)、[彩云天气](https://www.caiyunapp.com/dev_center/regist.html)、[Darksky(原forecast.io)](https://darksky.net/dev)和[心知天气](https://www.seniverse.com/pricing)。

个人感觉 AccuWeather 最好用，可惜免费版访问量限制得厉害，一天只允许 50 次，但数据全面(无地区限制)准确(来源应该是[中国气象局](https://baike.baidu.com/item/华风集团))；彩云天气还好，尤其自家 App 做的不错(卫星图是个亮点)；[Darksky](https://darksky.net/forecast/) 没其他问题，就是不够准，所以移除了；心知天气限制地区，也移除了