# coding   : utf-8 
# @Time    : 2020/1/27 17:29
# @Author  : 小迷弟
# @File    : try_prominx.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import requests

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36"}
parms = {"wd" : "python"}
url_temp = "https://www.baidu.com/s"
respons = requests.get(url_temp, headers=headers, params=parms)
print(respons.status_code)
print(respons.request.url)
# url = "https://www.baidu.com/s?wd={}".format("python")
# respons = requests.get(url, headers=headers)
# print(respons.status_code)
# print(respons.content.decode())