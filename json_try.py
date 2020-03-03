# coding   : utf-8 
# @Time    : 2020/1/30 19:13
# @Author  : 小迷弟
# @File    : json_try.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import  json
import requests
from paurse_url import paurse_url


url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Mobile Safari/537.36"}

response = requests.get(url, headers=headers)
ret = response.content.decode()
ret1 = json.loads(ret)
with open("douban.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=4))