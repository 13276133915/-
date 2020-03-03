# coding   : utf-8 
# @Time    : 2020/1/30 17:16
# @Author  : 小迷弟
# @File    : requests_小技巧.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import requests, time, json



url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)

dates = json.loads(requests.get(url=url).json()['data'])

print(dates.keys())


city_boss = dates['areaTree'][0]['children']
k = 0
for item in city_boss:
    if item['name'] in '江苏':
        break
    k += 1


for item in city_boss[k]['children']:
    if item['name'] in '盐城':
        for data in item['total'], item['today']:
            print(data)