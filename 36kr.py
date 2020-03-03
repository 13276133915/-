# coding   : utf-8 
# @Time    : 2020/1/31 2:15
# @Author  : 小迷弟
# @File    : 36kr.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import requests
import json
import re


url = "https://36kr.com/"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36"}
response = requests.get(url, headers=headers)
html_str = response.content.decode()
ret = re.findall("<script>window.initialState=(.*)</script>", html_str)[0]
with open("36kr.json", "w", encoding="utf-8") as f:
    f.write(ret)

ret = json.loads(ret)
print(ret)
