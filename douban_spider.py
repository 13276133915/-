# coding   : utf-8 
# @Time    : 2020/1/31 2:55
# @Author  : 小迷弟
# @File    : douban_spider.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import requests
import json
import time


url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
print(data)
print(data.keys())




